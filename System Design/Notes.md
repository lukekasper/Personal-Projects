## Scalability

#### Clones:
- Scalable web apps have multiple servers running the same codebase
- Each server must be identical, therefore cannot store any user or session data
- Data should be stored on a centrally managed database or persistent cache
	- Redis is a good option for cache
	- This central database/cache server should be in or near the datacenter hosting the servers for optimal performance
- Kubernetes/Docker can be sued to insure consistent deployment across different server nodes
- Amazon Machine Images (AMI): These are pre-configured virtual machine templates used to launch EC2 instances. If you're running Docker containers on EC2, an AMI ensures that all instances start with the same base configuration.
  
#### Database:
- After awhile, applications with a lot of requests may eventually slow down and break altogether.  This is often a result of the MySQL database schema
	- Use a NoSQL database like MongoDB
	- Joins will now need to be done in your application code
![image](https://github.com/user-attachments/assets/31dc1ec5-5fc2-4325-ae5c-6e98f7f99641)

#### Caching:
- Data retrieval should first check the cache, only when that is not available should it query the database
- Cache is much faster due to holding the dataset in RAM
- Redis or Memcache are the appropriate choices
- Cached Database Queries:
	- Store common database queries in RAM as cache
 	- Hashed version of the query is the cache key
  	- Drawback: when one piece of data changes (ie a table cell), you must delete all cached queries that may include that cell. This is difficult for complex queries
- Cached Objects:
	- Let the class assemble a dataset from the database and cache an instance of the class or the assembled dataset
 	- This allows you to easily remove the object whenever something changes
  	- Makes asynchronous processing possible
  		- Application just consumes the latest cached object and rarely needs to touch the database directly
  	 - Objects to cache:
  	 	- user sessions (never use the database!)
		- fully rendered blog articles
		- activity streams
		- user<->friend relationships
- Redis vs Memcache:
	- Redis has persistence, built-in data structures (lists and sets), and is more memory efficient
	- Memcache is highly scalable, has multithreading, simpler API
	
#### Asynchronism
- Async paradigm #1: do the time consuming work in advance and serve the finished product with a low request time
	- Ie generate the html of large web pages in advance using a backend or script and serve the static html
- Async paradigm #2: use a job queue and multiple worker nodes on the backend to process jobs
	- A computationally intensive task is requested by the user
 	- This job is sent to a queue on the backend while the user continues to browse the page
  	- Worker nodes are constantly checking the queue for new jobs, and when one is available they pick it up and execute
  	- When the job is complete, a signal is sent to the front end and the product is served
