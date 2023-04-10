## Intro to Kubernetes
- Open source container orchestration tool
- Helps manage many containerized applications in different environments
- Guaruntee: high availability, scalability, and disaster recovery
- Components:
  - Node: simple server (physical or virtual machine)
    - Pod: smallest unit of K8s; layer of abstraction over container
      - usually 1 application per pod (one for DB and one for JavaScript app)
      - Kubernetes acts as a virtual network, each pod gets its own internal (private) IP address
      - If pod dies (server crashes or runs out of resources), new pod is created with NEW IP address
  - Service: permenant IP address that is attatched to a pod (not connected to life of pod)
    - also serves as a load balancer
  - External service: opens app from an external (public) source
    - Ingress: external service calls first route to here, prior to being routed to service
      - allows for url domain names rather tha IP addresses
  - Internal service: for databases
    - database url typically defined within application
  - ConfigMap: external configuration of app
    - contains things like urls of databses
    - connect to pod
    - now adjustments to things like databse url is automatically updated in app (no rebuild required)
    - don't put credentials in config map!
  - Secret: config map for storing secret data (credentials), stored in a base64 encoded format
    - connected to pod also
    - use it as environmental variables or a properties file
  - Volumes: attatches a physical storage or hardrive to database pod; serves as a backup
    - can be local or remote (cloud)
  - Deployment: blueprint for replica of pod, for stateLESS apps
    - another abstraction on top of pods
    - makes it more convenient to interact with pods (in practice mostly work with these over pods)
  - StatefulSet: used to replicate databases, for stateFUL apps
    -  makes sure database read and writes are synchronized between replicas to avoid inconsistencies
    -  implementation is difficult, often times databases are hosted outside of K8s clusters
- Replicate everything to multiple servers to ensure high availability
  - connected to same service


## Kubernetes Architecture
- Node processes: must be installed on every node
  - Container runtime: ie) Docker
