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
    - Opportunity for queues:
        - Fan-Out Service:
            - Push tweet jobs [tweet_id, user_id, follower_id, op_type] to a queue
            - Have workers asynchronously process these to write to variuos user's home timelines
        - Notification service (discussed above)
    - Can use LRU cache to keep "hot" tweets or users in-memory for Services
    
