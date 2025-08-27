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
- Scaling:
    - Serve popular queries from an in-memory cache (Redis or Memcached)
    - Document and Reverse Index services would probably have their own db clusters attached
        - Would need to make use of sharding/federation
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
