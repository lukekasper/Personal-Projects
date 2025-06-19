## Scalability

#### Clones:
	- Scalable web apps have multiple servers running the same codebase
	- Each server must be identical, therefore cannot store any user or session data
	- Data should be stored on a centrally managed database or persistent cache
		○ Redis is a good option for cache
		○ This central database/cache server should be in or near the datacenter hosting the servers for optimal performance
	- Kubernetes/Docker can be sued to insure consistent deployment across different server nodes
	- Amazon Machine Images (AMI): These are pre-configured virtual machine templates used to launch EC2 instances. If you're running Docker containers on EC2, an AMI ensures that all instances start with the same base configuration.


#### Database:
	- After awhile, applications with a lot of requests may eventually slow down and break altogether.  This is often a result of the MySQL database schema
		○ Use a NoSQL database like MongoDB
		○ Joins will now need to be done in your application code
![image](https://github.com/user-attachments/assets/31dc1ec5-5fc2-4325-ae5c-6e98f7f99641)

### Caching:
	- Data retrieval should first check the cache, only when that is not available should it query the database
	- Cache is much faster due to holding the dataset in RAM
	- Redis or Memcache are the appropriate choices
	
