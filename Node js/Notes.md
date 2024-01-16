### Node Js Notes
Reference: https://www.youtube.com/watch?v=RLtyhwFtXQA

- EventEmitter class is used to drive event triggers and define custom events
- File system module (fs) is usesd to interact with files:
  - Create, write, rename, append, unlink (delete)
  - Streams are able to read and wrtie data in chunks more efficiently for large data files
    - used with "data" event handler
    - "pipe" method is used to send readstream data into writestream handler
    - can be combined with gzip to compress data
- http module creates an http web server
