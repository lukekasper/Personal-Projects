## System Design Solutions

### General Info
- Reading 1 MB sequentially from memory takes about 250 microseconds, while reading from SSD takes 4x and from disk takes 80x longer
- Sizing:
    - Currency/Datetime ~ 5 bytes
    - Char = 1 byte
    - Int = 4 bytes
    - Double = 8 bytes
    - Media ~ 1-10 KB

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
    - API: `$ curl https://search.com/api/v1/search?query=hello+world`
    - Response:
    ```
    {
    "title": "foo's title",
    "snippet": "foo's snippet",
    "link": "https://foo.com",
    },
    ...
    ```
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
        - API: `$ curl https://twitter.com/api/v1/search?query=hello+world`
        - Response: same as home timeline but tweets matching search criteria

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
- Database considerations:
     - User info (10 million) in SQL db
         - Schema:
         ```
         id int NOT NULL AUTO_INCREMENT
         created_at datetime NOT NULL
         last_update datetime NOT NULL
         account_url varchar(255) NOT NULL
         account_login varchar(32) NOT NULL
         account_password_hash char(64) NOT NULL
         user_id int NOT NULL
         PRIMARY KEY(id)
         FOREIGN KEY(user_id) REFERENCES users(id)
         ```
         - Create index on id, user_id, created_at (speed up lookups and keep in memory)
         - "user_id" seperate from "id" due to:
             - Security: don't want to expose internal db structure via API
             - Portability: can migrate data more easily
             - Third party: user_id may have meaning to other systems you are integrating with
     - Transactions in SQL db
         - Schema:
         ```
         id int NOT NULL AUTO_INCREMENT
         created_at datetime NOT NULL
         seller varchar(32) NOT NULL
         amount decimal NOT NULL
         user_id int NOT NULL
         PRIMARY KEY(id)
         FOREIGN KEY(user_id) REFERENCES users(id)
         ```
         - Create index on id, user_id, created_at
     - Monthly spending in SQL db
         - Schema:
         ```
         id int NOT NULL AUTO_INCREMENT
         month_year date NOT NULL
         category varchar(32)
         amount decimal NOT NULL
         user_id int NOT NULL
         PRIMARY KEY(id)
         FOREIGN KEY(user_id) REFERENCES users(id)
         ```
         - Create index on id, user_id
     - Atomic transaction data screams SQL! Cannot risk eventual consistency model with monetary data.
- Use cases:
    - User connects to a financial account:
        - Client sends request to Web Server (reverse proxy)
        - Web server forwards request to Accounts API server
        - Accounts API server updates SQL db accounts table with new info
        - API:
        ```
        $ curl -X POST --data '{ "user_id": "foo", "account_url": "bar", \
        "account_login": "baz", "account_password": "qux" }' \
        https://mint.com/api/v1/account
        ```
        - Service extracts transaction from account
    - Service extracts transactions from the account
        - Extract info when:
            - User first links account
            - User manually refreshes account
            - Each day for active users (past 30 days)
        - Steps:
            - Client sends request to web server
            - Web server forwards request to Accounts API
            - Accounts API places job on queue (RabbitMQ)
            - Transaction Service:
                - Pops job off queue and extracts transactions for that account
                    - Writes results to raw log file in object store
                - Uses category service to categorize each transaction
                    - Updates SQL "transactions" table with enriched transaction data (including category)
                    - Writes mapped intermediate data to a temp file storage (HDFS)
                        - Can use streaming option (Kafka) if needing real-time updates
                - Uses Budgest service to calculate monthly spending by category
                    - Injests intermediate mapped data (reads from HDFS)
                    - Reduces output by montly spending
                    - Budget service uses notification service to notify users if near or exceeding budget
                    - Updates SQL "monthly spending" table
                - Notifies users transactions have synced through Notification service
                    - Notification service uses a queue and downstream email/mobile push services to distribute notifications
    - Service recommends a budget
        - Create a budget template based on user defined income
        - User can override budget categories
        - Store results in buget_overrides table
        - Every time the Budget service recomputes a monthly spending, compare against the user budget
            - Send notifications when a defined threshold is met
            - Display metrics to user
    - User accesses summaries and transactions
        - Client sends request to web server, forwards to Read API
        - Read API:
            - Employs read-through cache to display content
          
- Service Implementations:
    - Category Service:
        - Create seller->category dict with most popular sellers:
        ```
        class DefaultCategories(Enum):

            HOUSING = 0
            FOOD = 1
            GAS = 2
            SHOPPING = 3
            ...
        
        seller_category_map = {}
        seller_category_map['Exxon'] = DefaultCategories.GAS
        seller_category_map['Target'] = DefaultCategories.SHOPPING
        ...
        ```
        - For sellers not in initial map, use user overrides:
        ```
        class Categorizer(object):

            def __init__(self, seller_category_map, seller_category_crowd_overrides_map):
                self.seller_category_map = seller_category_map
                self.seller_category_crowd_overrides_map = seller_category_crowd_overrides_map
        
            def categorize(self, transaction):
                if transaction.seller in self.seller_category_map:
                    return self.seller_category_map[transaction.seller]
                elif transaction.seller in self.seller_category_crowd_overrides_map:
                    self.seller_category_map[transaction.seller] = \
                        self.seller_category_crowd_overrides_map[transaction.seller].peek_min()
                    return self.seller_category_map[transaction.seller]
                return None

        class Transaction(object):

            def __init__(self, created_at, seller, amount):
                self.created_at = created_at
                self.seller = seller
                self.amount = amount
        ```
        - Min heap would allow lookups of top overrides in O(1)
        - "seller_category_crowd_overrides_map" gets populated through user interactions with the UI
            - Tracks all overrides by user and ranks them (maybe by frequency)

    - Budget Service:
        - Runs MapReduce job on raw transaction logs for that month to create montly aggregates
        - Writes data to monthly_spending aggregate table
        - Call budget service to re-run analysis if user updates a category
        ```
        class Budget(object):

        def __init__(self, income):
            self.income = income
            self.categories_to_budget_map = self.create_budget_template()

        def create_budget_template(self):
            return {
                DefaultCategories.HOUSING: self.income * .4,
                DefaultCategories.FOOD: self.income * .2,
                DefaultCategories.GAS: self.income * .1,
                DefaultCategories.SHOPPING: self.income * .2,
                ...
            }

        def override_category_budget(self, category, amount):
            self.categories_to_budget_map[category] = amount
        ```
- Considerations:
    - User updates a category manually:
        - Web server contacts accounts API
        - Accounts API puts job on queue to update that transaction
        - Rerun budget service to recompute statistics for that user/month including the updated transaction
            - Need to be careful how we incorporate the updated info with the out-of-date raw logs
    - Store monthly_spending in Analytics Database (Amazon Redshift or Google BigQuery)
        - May need to access and sum over monthly totals for ALL users to do a rollup
        - Can be very computationally expensive
    - Keep only a months worth of data in transactions table
        - Can rebuild for older transactions on-the-fly from object store (raw data)
    - Keep "hot" transactions in memory with refresh-ahead or LRU cache
    - Candidates for NoSQL:
        - Seller->Category maps: key-value, small, Redis
<img width="1308" height="1332" alt="image" src="https://github.com/user-attachments/assets/f4a19d62-115a-4205-8c03-af3da940ed27" />

### Social Network Data Structures
- Use Case: find shortest path between user and searched person
- Shard users across Persons servers and access with Lookup Service (can use consistent hashing scheme to do this)
    -  Client contacts web server, forwards request to Search API
    -  Search API forwards request to User Graph Service
    -  User Graph Service:
        - Uses Lookup Service to find Person Server where user is located
        - Retrieves list of user's friend_ids
        - Runs a BFS using user as source and friend_ids as first neighbors
            - To get neighbor from a node, User Graph Service will again need to contact Lookup Service/Person Servers to find that neighbors friend_ids
         
###### Implementations:
- Lookup Service:
```
class LookupService(object):

    def __init__(self):
        self.lookup = self._init_lookup()  # key: person_id, value: person_server

    def _init_lookup(self):
        ...

    def lookup_person_server(self, person_id):
        return self.lookup[person_id]
```
- Consistent Hashing:
```
import hashlib
import bisect

class ConsistentHashRing:
    def __init__(self, servers):
        self.ring = []
        self.server_map = {}
        for server in servers:
            key = self.hash(server)
            self.ring.append(key)
            self.server_map[key] = server
        self.ring.sort()

    def hash(self, key):
        """Returns a hash value in integer space"""
        return int(hashlib.md5(key.encode()).hexdigest(), 16)

    def get_server(self, user_id):
        """Find the server responsible for this user"""
        user_hash = self.hash(user_id)
        idx = bisect.bisect(self.ring, user_hash) % len(self.ring)
        return self.server_map[self.ring[idx]]
```
- Person Server:
```
class PersonServer(object):

    def __init__(self):
        self.people = {}  # key: person_id, value: person

    def add_person(self, person):
        ...

    def people(self, ids):
        results = []
        for id in ids:
            if id in self.people:
                results.append(self.people[id])
        return results
```
- Person:
```
class Person(object):

    def __init__(self, id, name, friend_ids):
        self.id = id
        self.name = name
        self.friend_ids = friend_ids
```
- User Graph Service:
```
class UserGraphService(object):

    def __init__(self, lookup_service):
        self.lookup_service = lookup_service

    def person(self, person_id):
        person_server = self.lookup_service.lookup_person_server(person_id)
        return person_server.people([person_id])

    def shortest_path(self, source_key, dest_key):
        if source_key is None or dest_key is None:
            return None
        if source_key is dest_key:
            return [source_key]
        prev_node_keys = self._shortest_path(source_key, dest_key)
        if prev_node_keys is None:
            return None
        else:
            # Iterate through the path_ids backwards, starting at dest_key
            path_ids = [dest_key]
            prev_node_key = prev_node_keys[dest_key]
            while prev_node_key is not None:
                path_ids.append(prev_node_key)
                prev_node_key = prev_node_keys[prev_node_key]
            # Reverse the list since we iterated backwards
            return path_ids[::-1]

    def _shortest_path(self, source_key, dest_key, path):
        # Use the id to get the Person
        source = self.person(source_key)
        # Update our bfs queue
        queue = deque()
        queue.append(source)
        # prev_node_keys keeps track of each hop from
        # the source_key to the dest_key
        prev_node_keys = {source_key: None}
        # We'll use visited_ids to keep track of which nodes we've
        # visited, which can be different from a typical bfs where
        # this can be stored in the node itself
        visited_ids = set()
        visited_ids.add(source.id)

        # Try to resume from cached layers
        while True:
            cached_layer = get_cached_layer(source_id, depth)
            if cached_layer:
                for node in cached_layer:
                    visited[node] = source_id  # Assume direct parent for simplicity
                queue = deque(cached_layer)
                depth += 1
            else:
                break

        while queue:
            node = queue.popleft()
            if node.key is dest_key:
                return prev_node_keys
            prev_node = node
            for friend_id in node.friend_ids:
                if friend_id not in visited_ids:
                    friend_node = self.person(friend_id)
                    queue.append(friend_node)
                    prev_node_keys[friend_id] = prev_node.key
                    visited_ids.add(friend_id)
        return None
```
- API: `$ curl https://social.com/api/v1/friend_search?person_id=1234`
- Response:
```
{
    "person_id": "100",
    "name": "foo",
    "link": "https://social.com/foo",
}
...
```
- Optimizations
    - Store complete or partial BFS traversals in memory cache (seed queue with this)
        - Can also precompute popular user graphs and store in NoSQL db
            - Have to be careful how we determine what to store (only depth of a few degrees, only so many nodes per layer, ect)
        - Only run live BFS if both cache and NoSQL hits fail
    - Bi-directional BFS search
    - Batch together Person Server lookups
        - Can do this for a single user request, or create a small window to batch requests across multiple users
        - Shard servers by geographic location to increase size of batches
            - Discuss tradeoff of this with consistent hashing scheme and scalability
            - Could do a middle-ground combined approach
    - Start BFS from user's with many friends (less degrees of seperation)
        - Maintain a key-val memory cache for users -> friends count mapping for fast lookups
        - Okay to have eventual consistency here
    - Can make user of Graph db (Neo4j) and graph query language (GraphQL) for optimal performance
<img width="774" height="1042" alt="image" src="https://github.com/user-attachments/assets/971a9317-3e61-456b-a883-454665eda75b" />
