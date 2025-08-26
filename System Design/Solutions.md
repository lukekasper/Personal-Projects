## System Design Solutions
### Web Crawler
- Key data structures (NoSQL)
    - links_to_crawl: uses heapq to maintain priority queue
    - crawled_links: map of url to page signature
- Key abstractions of Crawler Service
    - PageDataStore: interact with db
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
        - Crawl: extract next link from priority queue, determine if similar page has been crawled (reduce priority), call crawl_page on link
    - 
