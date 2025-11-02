#### Data Format
- Frame format: Fixed-size header + payload.
- Header fields:
  - Magic: 8 bytes (high-entropy sync marker)
  -  Version/flags: 2–4 bytes
  -  Sequence number: 8 bytes (per stream, monotonic)
  -  Timestamp: 8 bytes (producer clock or NIC PTP)
  -  Payload length: 4–8 bytes (network order)
  -  Header CRC: 4 bytes (optional)
  -  Payload CRC32C: 4 bytes
-  Validation rules:
  -  Length bounds: 0 < len ≤ max_frame_size
  -  Strict CRC checks: Header and payload
  -  Sequence continuity: Detect gaps and duplicates

#### Architecture:
- Data producer:
  - GRC RCC (4 independent channel streams)
- Transport layer:
  - UDP: if real-time requirements are desired
  - TCP: if minimal data loss is required
  - Kafka: optimal choice, slightly more complex
  - Maybe use an approach with UDP for real-time and a seperate TCP channel for archival backup
  - Can use Kafka brokers on the receiving end to write to files based on topics (channels)
- Receive layer:
  - One receiver per stream
  - Read data from socket and parse out header
  - Validate CRCs and check sequence continuity
  - On corruption, discard frame and move to next magic number
  - Push valid frames onto a queue
  - Apply back pressure when queue is full (by stopping the recv() calls)
- Buffering layer:
  - Decouple ingestion from IO file writes
  - SPSC ring buffer per stream (lock-free queue)
    - Boost supplies their own spsc lock-free queue
- Assembly Layer:
  - Drain queue in batch chunks
  - Assembles chunks into radar periodics using in-memory bounded data structure
  - Expose data loss to user
- Write Layer:
  - Drains complete periodic from assembly object
  - Batch several periods together to avoid expensive write calls
  - Flushes batch buffer and writes append-only bindary data to .dat file
  - Writer tracks size of data being written to file and starts a new one when threshold is reached
    - Allows for sooner offline processing of data

#### Multi-threading:
- One receive and one write thread per channel
- No mutexes needed due to lock-free SPSC ring buffer design

#### Previous Setup:
- Previous setup used mutex to control read/writes to a shared data object
  - Receiver would flush buffer once chunk sized was reached
  - Use mutex on shared data object
  - Release object once written to
  - Writers would be looking for a full periodic return, and use mutext to write shared object to a file
  - Created lock contention
- No distinct seperation of layers/services
- Also no strict checking on data integrity or magic number implementation
- No batching of writes or file chunking
