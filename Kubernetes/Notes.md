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
  - Kubelet: interacts with both container and node
    - responsible for starting a pod with a container inside and assigning resources (like CPU, RAM, storage) from the node to the container
  - Kube proxy: forwards requests between pods
- Master processes:
  - API server: cluster gateway
    - interact externally with API server using a client (dashboard, cmd line tool, or Kubernetes API)
    - gets initial request for updates to cluster or queries
    - acts as gatekeeper for authentication
  - Scheduler: recieves requests from API server and sends scheduling requests onto pods
    - intelligently determines where to schedule next pod based on resource availability
    - executes request through Kubelet on that node
  - Controller manager: detect state changes (like pods crashing) and tries to recover state
    - makes request to scheduler to reschedule dead pods -> Kubelet
  - etcd: key-value storer of cluster state (cluster brain)
    - when state changes happen to pod, values get updated in etcd
    - provides the insight into what resources are available on each node, cluster health, did the state change
    - does not store actual application data
- Usually multiple master nodes for backup purposes
- Less resources for master nodes (no actual application data and processes)
- To make a new node:
  - get bare server
  - install necessary master/worker node processes
  - add it to the cluster


## Minikube and Kubectl
- Minikube: way to test cluster setup locally (master and worker processes run together on one machine)
  - ran through a virtual box on laptop
- kubectl: command line tool for K8 cluster
  - used to interact with minikube cluster
  - can be used for other types of clusters as well (ie cloud)
- Steps for installation:
  - minikube: https://bit.ly/38bLcJy 
  - kubectl: https://bit.ly/32bSI2Z
- Interacting with cluster (kubectl):
  - interact with deployment -> manages replicaset -> manages pod -> abstraction of a container
    - everything below deployment is managed automatically by kubernetes
  - debugging tips:
    - use "kubectl logs [pod name]" to log pod output
    - "kubectl exec -it [pod name] -- bin/bash" to get terminal of container
  - in practice, create a deployment using a configuration file to specify things like name, image, and options for deployment
    - kubectl apply -f [config file name]: to execute configuration file

## YAML Configuration Files:
- Metadata: things like name of the component
- Specification: kinds of configurations you want to apply
  - attributes are dependent on the kind of component
- status: automatically generated by kubernetes (comes from etcd)
- use yaml online validator to make sure file syntax is correct
- store config file with code
- blueprints for deployments are defined in the template portion of config file under Specification
  - has its own metadata and specification (basically a nested config file)
- these are applied through labels (metadata) and selectors (specifications)
  - in metadata, give component a key-value pair under label (app: nginx)
  - the label is then matched by the selector
  - for a service, the selector is matched with the label of the deployments it needs to communicate with
- services have their own ports, and targetPort (port numbers of the pods they intend to connect to, specified by deployment yaml)
  - use: kubectl describe service nginx-service and kubectl get pod -o wide to ensure pods and services are communicating to the same ports