## System Design Solutions
### Web Crawler
- Key data structures (NoSQL)
    - links_to_crawl: use heapq to maintain priority queue
    - crawled_links: map of url to page signature
- Key abstractions of Crawler Service
    - PageDataStore: interacts with db
        - Add/remove links to crawl
        - Reduce link priority to avoid cycles
        - Extract max priority from links_to_crawl
        - Insert crawled link
        - Determine if we've crawled a similar page based on signature
    - Page: page object
        - Url, contents, child_urls, signature
    - Crawler: contains PageDataStore, reverse_index_queue, doc_index_queue
        - Create signature (based on page url/contents)
        - Crawl page: add child urls to links_to_crawl db, create signature, remove link from links_to_crawl, add link to crawled_links
            - As it crawls each page, can populate reverse_index_queue and doc_index_queue with page contents/url
        - Crawl: extract next link from priority queue, determine if similar page has been crawled (reduce priority), call crawl_page on link
            - Reduction in priority allows the url to be checked again later to refresh content
- Reverse Index / Document Queues: seperate service (RabbitMQ)
- Reverse Index Service:
    - Consumes reverse index queue
    - Runs MapReduce job:
        - Maps words to doc_id (or url)
        - Reduces index to (word, [doc_ids])
    - Ranks matching results based on query input and returns top ones
- Document Index Service:
    - Consumes document index queue
    - Runs MapReduce job:
        - Maps doc_id (or url) to metadata
        - Reduces or merges metadata for each document
    - Returns titles and page snippets for rendering results
- Query API:
    - Client sends request to web server (running as reverse proxy)
    - Web server forwards request to query API server
    - Parses query: removes markup, breaks text into term, fixes typos, normalizes capitalization, converts query into boolean operations
    - Use reverse index service to find matching webpages
    - Use document service to return snippets
- Other considerations:
    - Can use fetch to get the url content, BeautifulSoup library to parse the content and extract child links by finding "<a href" tags
    - crawled_links can have a timestamp field to indicate when it was last crawled
        - Can compare this with preset ttl to determine if page refresh is needed
    - Crawler is seeded an input, then it is self-feeding; no direct interaction from user
    - Crawler can use MapReduce to ensure only unique urls get fed into links_to_crawl
        - Of the extracted urls, discard any that appear more than once to reduce load on server
    - Brief discussion of public REST API response structure
    - Discuss optimizations for caching and db replication strategies
    - Backpressure to slow down crawler if queues get full
- Scaling:
    - Serve popular queries from an in-memory cache (Redis or Memcached)
    - Document and Reverse Index services would probably have their own db clusters attached
        - Would need to make use of sharding/federation
        - Can cache popular query results using LRU scheme
    - Crawler service can maintain in-memory cache of DNS lookups
        - Can do proactive (refresh ahead) cache to keep popular sites in-memory
    - UDP could be used for internal service communication in some areas to boost performance
        - DNS lookup, push results to queue, query API to services, ect
    - Use connection pooling to keep TCP connections open when crawling multiple pages on the same host/site
        - Reduce TCP overhead
     
<img width="1078" height="1304" alt="image" src="https://github.com/user-attachments/assets/d955e7b5-5909-4641-a110-6c39c8da2f01" />

- Pipelines:
    - Search: Client -> Web Server -> Query Service -> Reverse Index (returns ranked urls) / Document Service (returns snippets) -> Back to up chain to client
    - Indexing: Reverse Index / Document Service -> pops job off queue -> generates reverse index -> writes/updates data in persistent storage and adds hot items to in-memory cache
    - Crawling: Crawler is seeded with inputs -> pops priority item off links_to_crawl -> determines if similar page is in crawled_links (signature based) -> fetch wepbage and parse html -> use content to populate document and reverse index queues -> extract child links to s3 or some other temp storage -> runs MapReduce job (asynchronously) -> add child links to links_to_crawl -> create signature, remove url from links_to_crawl, add url to crawled_links

- MapReduce: use MRJob library
```
class RemoveDuplicateUrls(MRJob):

    def mapper(self, _, line):
        yield line, 1

    def reducer(self, key, values):
        total = sum(values)
        if total == 1:
            yield key, total
```
Calling MapReduce job:
```
def run_dedup_job(input_uri, output_uri):
    job = RemoveDuplicateUrls(args=[
        input_uri,
        '--output-dir', output_uri,
        '--runner', 'hadoop',
    ])
    with job.make_runner() as runner:
        runner.run()
```

### Twitter Timeline and Search
- Data Stores/Structures:
    - User's tweets: row like data object stored in SQL db containing full tweet info
        - High-write, append-only
    - Users: row like data object stored in SQL db containing user metadata
        - Low-write, high-read
    - User home timeline:
        - Each user has their own timeline of tweets from their followers
        - Tweet is a Redis list in memory cache: [tweet_id, user_id, meta]
        - Allows for fast access
    - User Graph: Graph Store (Neo4j) and cached in-memory
    - Search Index: ElasticSearch cluster
    - Object Store: s3 bucket
    - Notification Service:
        - Pulls from queue populated by fan-out service (RabbitMQ)
        - Uses reverse-index (NoSQL db/cache) with key-value structure (author_id: [subscriber_ids])
- Use cases:
    - User posts a tweet:
        - Client posts tweet to Web Server (reverse proxy)
        - Web server forwards request to Write API server
        - Write API stores tweet in user's timeline in a SQL db
        - Write API contacts Fan Out Service:
            - Queries User Graph Service to find user's followers
            - Stores tweet ids in home timeline of each of the user's followers in memcache
                - O(n) -> 1000 follwers = 1000 lookups and inserts
            - Stores tweet ids in Search Index Service to enable fast searching
            - Stores media in Object store
            - Uses Notification Service to send push notifications to followers
                - Uses Queue to asynchronously send out notifications
                - Notification processes queue event, does reverse lookup on user's subscribed to author's tweets, sends tweet metadata to mobile/email delivery services
        - API:
        ```
        $ curl -X POST --data '{ "user_id": "123", "auth_token": "ABC123", \
        "status": "hello world!", "media_ids": "ABC987" }' \
        https://twitter.com/api/v1/tweet
        ```
        - Response:
        ```
        {
            "created_at": "Wed Sep 05 00:37:15 +0000 2012",
            "status": "hello world!",
            "tweet_id": "987",
            "user_id": "123",
            ...
        }
        ```
    - User views home timeline:
        - Client requests to view home timeline
        - Web server forwards request to read api
        - Read api contacts Timeline Service:
            - Get timeline data for that user stored in Redis cache O(1)
            - Queries Tweet Info service to get tweet info via tweet ids O(n)
                - Use multiget to query SQL db where full tweet info is stored
                - May also have tweet-level cache sitting in front of this to boost performance on popular tweets
            - Queries User Info service to get user info via user ids O(n)
                - Same concept as tweet info service retrieval
        - API: `$ curl https://twitter.com/api/v1/home_timeline?user_id=123`
        - Response:
        ```
        {
            "user_id": "456",
            "tweet_id": "123",
            "status": "foo"
        }
        ...
        ```        
    - User views their timeline:
        - Client requests their timeline
        - Web server forwards request to Read API
        - Read API looks for tweets from that user in memory cache, otherwise pulls them from SQL db
    - User searches for tweets:
        - Client provides a query
        - Web server forwards request to Search API
        - Search API processes query (remove markdown, extract query params, convert to boolean, correct spelling, standardize capitalization)
        - Search API contacts Search Service to gather tweet info based on query params
        - Search API contacts the Tweet Info Service with the tweet ids and User Info Service with the user ids to get the full tweet info for rendering

- Database discussion:
    - User tweets can be stored in a SQL db
        - Predictable write pattern
        - Data is bounded to 1 user
        - Favor strong consistency, user posts a tweet and expects it immediately visible
    - Fanout (~60,000 tweets per second) will overload RDBMs, use NoSQL and Redis
        - Eventual consistency model allows for fast writes and eventual consistency to followers
        - Eliminates need for joins
        - Can use append-only operations, with compaction/cleanup later
- Other considerations:
    - Discussion on REST API
    - Discussion of cache data structure
    - Internal communications use RPC
    - Race condition for celebrity users:
        - Could take minutes for fan-out service to populate all follower's home timeline objects
        - If someone replies to the tweet before it reaches everyone's home timeline, you could see the reply before the initial tweet
        - Solution: keep a "recent activity" append-only log (ie Kafka) with ttl of a few minutes
            - At serve-time, timeline service can search this log for tweets from people the user follows
            - Compare this with tweet ids in the home timeline data object
            - If there are any deltas, add tweet ids from the recent activity log and sort based on timestamp
            - Then hydrate all tweets with Tweet Info Service
    - Discuss optimizations for caching and db replication strategies
    - Discuss backpressure considerations for queues
- Optimizations:
    - Keep only several hundred tweets for each home timeline in memory cache
    - Keep only active users home timeline info in memory cache
    - Tweet and User Services can keep recent tweets/active users in Redis db for faster access
        - Can do this through query-level caching (hash query)
    - Opportunity for queues:
        - Fan-Out Service:
            - Push tweet jobs [tweet_id, user_id, follower_id, op_type] to a queue
            - Have workers asynchronously process these to write to variuos user's home timelines
        - Notification service (discussed above)
    - Can use LRU cache to keep "hot" tweets or users in-memory for Services
    - Cache strategies:
        - Write through: graph service, home timeline, user timeline
            - Involve updates and don't want stale data, data is available immediately in cache
            - Stale data could result in missed fan-outs
        - Read through: Tweet/User info service
            - Objects are immutable after creation, can lazy-load and keep hot/recent tweets in memory using LRU/TTL
<img width="1348" height="1390" alt="image" src="https://github.com/user-attachments/assets/aa09e79d-d957-4cbc-a1df-1bb7076002c5" />

### Paste Bin
- Use Cases:
    - User paste's content
        - Client sends request to web server (reverse proxy)
        - Web server forwards request to Write API
        - Write API:
            - Generates a unique url:
                - Checks if url exists in db, if so generate a new one
            - Writes entry to SQL databse: shortlink (primary key), expiration time (optional), timestamp, paste path
                - Create additional index on timestamp to speed up querying and keep data in memory
            - Saves content to object store
            - Returns url
        - API: `$ curl -X POST --data '{ "expiration_length_in_minutes": "60", "paste_contents": "Hello World!" }' https://pastebin.com/api/v1/paste`
        - Response: `{"shortlink": "foobar"}`
    - User searches a url:
        - Client sends request to web server
        - Web server forwards request to Read API
        - Read API:
            - Checks SQL db for url
            - If it exists, fetch content from object store based on url path and render
            - If not, return an error message
        - API:
        `$ curl https://pastebin.com/api/v1/paste?shortlink=foobar`
        - Response:
        ```
        {
            "paste_contents": "Hello World"
            "created_at": "YYYY-MM-DD HH:MM:SS"
            "expiration_length_in_minutes": "60"
        }
        ```
    - Analytics on number of visits to a url per month:
        - Use MapReduce job on Web Server Logs
            - Scrape server logs and extract relevant lines with a server url
            - Map url/month and reduce by summing hits on a url in a given month
            ```
            class HitCounts(MRJob):
                def extract_url(self, line):
                    """Extract the generated url from the log line."""
                    ...
            
                def extract_year_month(self, line):
                    """Return the year and month portions of the timestamp."""
                    ...
            
                def mapper(self, _, line):
                    """Parse each log line, extract and transform relevant lines.
            
                    Emit key value pairs of the form:
            
                    (2016-01, url0), 1
                    (2016-01, url0), 1
                    (2016-01, url1), 1
                    """
                    url = self.extract_url(line)
                    period = self.extract_year_month(line)
                    yield (period, url), 1
            
                def reducer(self, key, values):
                    """Sum values for each key.
            
                    (2016-01, url0), 2
                    (2016-01, url1), 1
                    """
                    yield key, sum(values)
            ```
    - Delete expired links:
        - Scan db for timestamp + expired time > current time: O(logN)
        - Delete these entries or mark as expired
- Generate unique url:
    - Use MD5 hash scheme using user's ip address + timestamp (16 bytes)
    - Use Base62 to encode MD5 hash to make it compatible with url (no special characters)
        - Take first 7 values of result (62^7 possibilities)
    ```
    import hashlib
    import string
    
    # Base62 character set: 0-9, A-Z, a-z
    BASE62_ALPHABET = string.digits + string.ascii_uppercase + string.ascii_lowercase
    
    def base62_encode(num):
        """Encodes a positive integer into a Base62 string."""
        if num == 0:
            return BASE62_ALPHABET[0]
        
        base62 = []
        while num > 0:
            remainder = num % 62          # modulus to get the digit
            num = num // 62               # integer division for the next loop
            base62.append(BASE62_ALPHABET[remainder])
        return ''.join(reversed(base62))
    
    def md5_to_base62(input_str, length=8):
        """
        Hashes the input string with MD5, converts to Base62,
        and returns the first `length` characters.
        """
        # Step 1: MD5 hash (hex string)
        md5_hash = hashlib.md5(input_str.encode('utf-8')).hexdigest()
        
        # Step 2: Convert hex string to integer
        num = int(md5_hash, 16)
        
        # Step 3: Encode integer to Base62
        base62_str = base62_encode(num)
        
        # Step 4: Return shortened key
        return base62_str[:length]
    ```
        
- Scaling:
    - Collecting server logs across multiple web servers could involve pushing them to a centralized storage (HDFS) and running MapReduce on all log files
        - Web server logs are now being kept in their own object store
    - Use analytics database (Amazon Redshift or Google BigQuery) for monthly hits data
    - If collecting monthly analytics:
        - Can update once per month if fresh analytics within the month are not required
        - Can store daily hits in analytics database and combine during query time for that month
    - Can create an asyncronous workflow for writes to speed up performance:
        - User requests a write, and synchronously a shortlink is generated and sent in response to user
        - WriteJob is created and pushed to queue, worker node picks this job up to write data to SQL db and Object store
<img width="936" height="1360" alt="image" src="https://github.com/user-attachments/assets/5cbd1a20-73d7-40a4-83b3-05b6f616c22b" />

### Mint
