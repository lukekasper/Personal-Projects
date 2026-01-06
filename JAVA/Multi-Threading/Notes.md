### Notes
- https://blog.seancoughlin.me/multithreading-in-java-and-spring-boot
- Async annotation abstracts away most async code for Spring Boot
  - Allows methods to execute on a seperate thread to not block main program execution
- `ThreadPoolTaskExecutor` allows customization of production thread pools
  - Core pool size: Minimum number of threads that will always be available.
  - Max pool size: Maximum number of threads that can be created.
  - Queue capacity: How many tasks can be queued before new threads are created.
  - Thread name prefix: Custom naming pattern for threads in this executor
- Optimal parameters:
  - Short, non-blocking tasks (ie logging): 2, 5, 50
  - I/O bound tasks (file reads, db queries): 4, 10, 100
  - CPU intensive (complex calculations/image processing): # of CPU cores, # of CPU cores, 0 or very small (1-10)
  - Long-running blocking tasks (external API calls, large data processing): 5, 20, 200
  - High Concurrency (thousands or requests for a web app): 10, 50, 500+
- Can use `@Scheduled` annotation to schedule background jobs
- Use `TaskExecutor` to execute tasks without dealing with Thread management
- If multiple threads are touching a shared muteable resource, must use "synchronization"
  - Should be rare as most state lives in resources like: databse, distributed cache, queues, ect.
- Common Thread Safety Issues:
  - Race Conditions: Occurs when two or more threads access shared data and try to change it at the same time.
  - Deadlocks: Happen when two or more threads are blocked forever, waiting for each other to release resources.
  - Memory Consistency Errors: Result when multiple threads access shared variables without proper synchronization.

### Example
https://github.com/Java-Techie-jt/order-batch-processing
https://github.com/Java-Techie-jt/api-performance-demo
