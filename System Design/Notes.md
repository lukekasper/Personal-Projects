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
- Stores data in a key-value pair framework in the servers RAM
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
 
#### Web Hosting
- What to look for:
	- SFTP vs FTP: need to have user info and passwords encrypted
 	- Shared host vs virtual private server (VPS)
		- VPS: you get your own slice of the server in an isolated enviornment
  		- Means you don't need to contend for resources
		- Data will still not be private from the web hosting company itself (can reboot machine in single user mode)
- Scaling:
	- Vertical: add more RAM or performance per machine
 		- Only can upgrade machines so much
   		- Solid State Drives (SSDs): provide faster disk writing operations, good for database servers; smaller storage size
 	- Horizontal: add more servers
  		- Load balancer disdistributes inbound requests across webservers
    			- Can return ip address of load balancer not individual servers
				- Can have private ip addresses for servers
      			- Return ip address of a different server each time
- Load balancing
	- AWS Elastic Load Balancer is one common software solution
	- Round robin:
		- Processing load is not evenly distributed across servers
		- Ip addresses from DNS request get cached by browser/OS, leading to the same server getting returned each time
		- Let load balancer do the round robin to get around ip caching
	- Sessions will break with this model, one server may have a session and when you get redirected to a new server it will not have session data
	- How to resolve sticky session problem: visiting a site multiple still leads to the same session data and same backend server
 		- Cookies: a small piece of data that a website/server stores on your device through your web browser
   			- Can store a hash of the server's ip or id in the cookie during the initial user request
      			- This then gets sent back to the load balancer during subsequent requests
         		- The load balancer then uses this hash to discern the server ip address with the user's session
   		- Caching: can store a user's session data in RAM
     			- Due to RAM constraints, cache can get too large for the machine
       			- Can use something like an LRU cache to clear out the oldest objects (linked list)
	- Load balancers also come with redundancy (Active-Active or Active-Passive) to reduce single point of failure
 		- Heartbeats between balancers to determine status
- MySQL storage:
	- Archive engine: automatically compresses data by default
		- Slower to query but uses less disk space
   		- Useful for log files, where database writes are common but rarely need to query the data
   	- Replication:
   		- Master-Slave:
   	 		- Master is written and read from but replicates data to slaves for redundancy
   	   		- Can specialize slaves for specific operations (read vs write) to increase performance
   	     		- Still single point of failure on master
		- Master-Master:
   			- Increases redundancy to eliminate single point of failure
   	  		- Heartbeats between servers to determine status
   	    		- Requires consistent replication/synchronization
- Partitioning: allows the load balancers or servers to handle parts of the workload based on logical divisions
	- Ie users A-M on one cluster and users N-Z in another
 	- Increases performance and redundancy
- High availability is the idea of servers/databases checking eachother for heartbeats to ensure minimal downtime
	- In addition to scalability, redundancy is critical to reducing single point of failures
 	- Need redundancy in web servers, database servers, load balancers, switches, and datacenters!
  	- Availability zones that AWS provides takes care of redundancy for datacenters
  	- DNS can provide load balancing for different datacenters based on geographical location
- Security:
	- Firewall only allows TCP.80 and 443 connections
 		- TCP 80 is default port for HTTP traffic and port 443 is default port for SSL (HTTPS traffic)
   		- May want to allow port 22 for ssh or SSL based VPN for connecting to datacenter remotely
	- Traffic from load balancers to web servers is TCP 80 only
 		- Less of a need to encrypt traffic once its within the datacenter
	- Expensive load balancers up front can handle cryptogrophy and SSL certs
 	- Traffic from web servers to databases are TCP 3306 (SQL queries)
  	- Switch can typically handle firewall concerns
  	- Principal of least privilege implies we want to limit access wherever possible 

#### High Level Trade-Offs
- Performance vs Scalability:
	- Scalability: adding more resources leads to a proportional increase in performance
 	- Performance: handling more or larger units of work
  	- For high availability, good scalability means adding more resources to facilitate redundancy does not lead to a loss of performance
  	- More requests, larger datasets, or additional nodes for redundancy can impact code performance
  	- Heterogeneity: some nodes will be able to process faster or store more data than other nodes in a system
  		- This can be due to newer/better hardware becoming available for some nodes
		- Algorithms that rely on uniformity either break down under these conditions or underutilize the newer resources
  	- Must architect programs early on to account for scalability concerns
- Latency vs Throughput:
	- Latency: time to perform some action or to produce some result
 	- Throughput: number of such actions or results per unit of time
  	- Generally, you should aim for maximal throughput with acceptable latency
- Availability vs Consistency:
	- Consistency: every read receives the most recent write or an error
 	- Availability: every request receives a response, without guarantee that it contains the most recent version of the information
  	- Partition Tolerance: the system continues to operate despite arbitrary partitioning due to network failures
  	- CAP Theorem states: in a distributed system, you can only have two out of the following three guarantees across a write/read pair
  		- Consistency, Availability, and Partition Tolerance
  	 	- Networks are unreliable, must tolerate partitions
  	- CP: consistency and partition tolerance
		- Waiting for a response from the partitioned node might result in a timeout error.
  		- CP is a good choice if your business needs require atomic reads and writes.
 	- AP: availability and partition tolerance
		- Responses return the most readily available version of the data available on any node, which might not be the latest.
  		- Writes might take some time to propagate when the partition is resolved.
		- AP is a good choice if the business needs to allow for eventual consistency or when the system needs to continue working despite external errors.
	- Eventual consistency: rely on a background process to synchcronize data between servers
 		- Assume some time between requests is acceptable to allow process to synchronize data
	- Consistency Patterns
 		- Weak consistency: after a write, reads may or may not see it. A best effort approach is taken.
   			- Seen in systems such as memcached. Works well in real time use cases such as VoIP, video chat, and realtime multiplayer games
      			- Ie) if you are on a phone call and lose reception for a few seconds, when you regain connection you do not hear what was spoken during connection loss.
         	- Eventual consistency: after a write, reads will eventually see it (typically within ms). Data is replicated asynchronously.
          		- Seen in systems such as DNS and email. Works well in highly available systems.
            	- Strong consistency: after a write, reads will see it. Data is replicated synchronously.
             		- Seen in file systems and RDBMSes. Works well in systems that need transactions.
       - Availability Patterns
       		- Fail-Over:
         		- Active-Passive: only active serves requests. Downtime is dependent on if passivve needs to do a hot or cold boot
           		- Active-Active: application logic or DNS service needs to know of both servers
       			- Disadvantages:
       				- Fail-over adds more hardware and additional complexity
       				- There is a potential for loss of data if the active system fails before any newly written data can be replicated to the passive
         	- Replication: Master-Slave and Master-Master (discussed more in database section)
			
   			<img width="272" alt="image" src="https://github.com/user-attachments/assets/129f203d-bc5d-42a1-9fb5-3a8fe0d6ab1a" />

	- Availability in parallel vs in sequence:
   		- If a service consists of multiple components prone to failure, the service's overall availability depends on whether the components are in sequence or in parallel
     		- Sequence: overall availability decreases when two components with availability < 100% are in sequence
       			- Availability (Total) = Availability (Foo) * Availability (Bar)
          	- Parallel: overall availability increases when two components with availability < 100% are in parallel
          		- Availability (Total) = 1 - (1 - Availability (Foo)) * (1 - Availability (Bar))
       
#### DNS
![image](https://github.com/user-attachments/assets/cab327f0-c0be-4d38-ba72-b5670da2e051)
- Domain Name System (DNS): translates a domain name to an ip address
- DNS can be cached by lower-level DNS servers or by browser/OS for a certain amount of time based on TTL properties
- NS record (name server): Specifies the DNS servers for your domain/subdomain.
- MX record (mail exchange): Specifies the mail servers for accepting messages.
- A record (address): Points a name to an IP address.
- CNAME (canonical): Points a name to another name or CNAME (example.com to www.example.com) or to an A record.
- DNS services: CloudFlare, Route 53
- Different methods for routing:
	- Round robin: distributes requests cyclically across servers
 	- Weighted round robin: accounts for servers with more CPU/RAM and gives those extra connections
  		- Must specify weights in advance based on server specs
    		- Sometimes beneficial to use this if you want to reserve one server for business critical applications (less connections
      		- Can prevent sending requests to servers under maintenance (weight=0)
	- Least connections: distribute traffic based on number of active connections rather than cyclically on new requests
 	- Weighted least connections: similar to weighted round robin
  	- Random: randomly assigns connections
  	- Latency-based routing: use latency records to determine which connection will have the best performance
  		- Route 53 DNS can accomplish this with an AWS elastic load balancer
  	 	- Latency records are based on measurements taken over time
  	- Geolocation-based: choose server based on location of users (where request originates from)
  		- Localize content (like display web page in the language of the user)
  	 	- Restrict content distribution to locations where you have distribution rights
  	  	- Restrict endpoints by location so user's get predictably routed to the same node
  	  	- Maps ips to a location; some ips won't be mapped though so need a default node to handle these cases
- Disadvantages:
	- Some delays from accessing a DNS, mitigated through caching
	- DNS server management could be complex and is generally managed by governments, ISPs, and large companies:
 		- Level 1: root servers; highly guarded; all other DNS servers cache from these
		- Level 2: secondary servers cache from root and are thus faster; managed by govs, ISPs and companies
  		- Domain name registration:
    			1. Register domain name registar
      			2. Registar sends a request to ICANN
      			3. Directs associated root server to add an entry based on Top Level Domain name (TLD)
      			4. Secondary servers cache this
      
