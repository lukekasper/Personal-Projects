https://www.youtube.com/watch?v=X48VuDVv0do    
https://gitlab.com/nanuchi/youtube-tutorial-series/-/tree/master/

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
  - use: "kubectl describe service nginx-service" and "kubectl get pod -o wide" to ensure pods and services are communicating to the same ports
  - specify selector as the label of the pod you want to connect to
- "deployment nginx-deployment -o yaml > nginx-deployment-result.yaml": get updated yaml status of deployment and save result
  - in order to copy deployment (blueprint), must clean status part of config file first


## Kubernetes Components Demo:
- go on "hub.docker.com" to determine what ports/environmental variables are available for a given image (ie mongo)
- don't want to define usrname and password info in config file
  - make secret config file to store usrname and password info and reference it in the yaml config file
  - values must be base64 encoded (not plain text)\
    - do this in terminal with "echo -n 'username' | base64" and "echo -n 'password' | base64" and paste into secret config file
- can put multiple documents in one file in yaml using "---" to seperate documents
  - deployment and service are usually combined
- reference value for something like mongo db server (service name) should be kept in config map not in yaml file itself
  - allows other pods to refernce this value and avoids having to update multiple yaml files on change
  - order matters, so must have config map in cluster before deploying yaml file that references it
- to make an external service:
  - in specification section (spec), add "type: LoadBalancer" below selector
    - assigns service an external IP address
  - then apply a third port
    - nodePort: # (some number between 30000-32767) which is what will be accessed by the browser
  - minikube service mongo-express-service will then make the external service in minikube

## Namespaces
- a way to organize resources (virtual cluster inside of a K8 cluster)
- default namespaces:
  - kube-system: not for user use, do not modify
  - kube-public: publicly accessible data
    - contains a config map with cluster info (even without authentication
  - kube-node-lease: contains info about nodes availability (heartbeat)
  - default: created resources are here
- kubectl create namespace <name>: to create new namespaces
- uses:
  - way to group resources
  - multiple teams
  - resource sharing: staging and development or blue/green deploment (two versions of production environments)
  - emply access or resource limits on certain namespaces
- cannot access most resources from another namespace
  - each namespace must define its own config map and secret
- can apply namespace in config file under metadata with: namespace: <name>
- use kubens to change default namespace to desired namespace and avoid having to specify -n <namespace> with each command

## Ingress:
- used to have a url in browser rather than IP address (like with an external service)
  - connects to with an internal service to connect to K8 pods
- yaml file configuration:
  - host: is what user will enter into browser (must be a valid/registered domain address)
    - map domain name to IP address of node you want to be the entry point to your cluster
  - backend: is what service request will be redirected to
    - service should be internal service name, and port should be the port of that internal service
- steps:
  1) request from browser to ingress
  2) request get forwarded to internal service
- also need an implementation for ingress (or ingress controller)
  - another pod or set of pods running in K8 cluster
  - does evaluation and processing of ingress rules, and manages redirections
  - is the entrypoint to the cluster
  - must download and install controller from third party vendor (or K8s nginx controller)
  - must consider the environment in which your cluster is running
    - if on a cloud, they will implement a load balancer (saving you the need to do that) which will redirect requests to the controller
- creating ingress rules
  - create a ingress yaml file in same namespace as service/pod
  - define rules in specification (spec)
  - set http forwarding to the internal serviceName and port you want to access
  - must define IP address mapping in /etc/hosts file (sudo vim /etc/hosts)
    - find using "kubectl get ingress -n <namespace>"
    - insert IP address and url mapping (esc, :wq will exit editor)
- default backend exists which can be used to define custom error messages for incorrect url pathways
  - make internal service with name "default-http-backend" and same port number (80)
- multiple paths for the same host:
  - can define seperate pathways using "paths: /path1" and send request to different port# and K8 services
  - can also define seperate hosts if multiple sub-domains are required
- to configure TLS certifficate (for https forwarding), define tls section in spec above rules and reference secretName
  - this contains TLS certificates (02:23:30)
  
## Helm
- package manager for Kubernetes (ie to package yaml files and distribute in public/private repositories)
- helm charts: standard bundle of K8 yaml files which includes things like config map, secret, ect
  - available on public repositories to download
  - things like database apps (MySQL) or Monitoring Apps (Prometheus) have helm charts available
  - find them in cmd line using: helm search <keyword> or at Helm Hub
- templating engine: way to define a common blueprint for similar microservices to avoid having to create yaml files for each one
  - dynamic values are replaced by placeholders {{ .Values... }}
    - .Values is an object based on values supplied by values yaml file or through cmd line using "--set" flag
    - values.yaml file is used to fill in template placeholders
    - practical for CI/CD (use template files in build pipeline)
- useful for same application across different environemnts (or K8 clusters)
- structure:
  - name of chart
    - chart.yaml: meta info about chart (name, version, dependencies, ect)
    - values.yaml: values for template files (default values to override
    - charts folder: chart dependencies (if chart is dependent on another chart)
    - templates folder: where template files are stored
      - helm install <chartname> will fill template files with values from values.yaml
      - can have other files like licenses or readme as well
- can provide values during install cmd with: `helm install --values=my-values.yaml <chartname>`
  - can use this to redefine values in default values.yaml file
  - this will merge two values files into a .Values object
- can also provide values directly in cmd line with: `helm install --set version=2.0.0`
- helm version 2 allows for release management by tracking chart executions (Tiller)
  - can rollback to previous versions if necessary
- helm 3 removed Tiller due to security concerns (too much control within K8 cluster)
  
## Volumes
- no default data persistence between pod restarts (can lead to loss of data in databases)
  - if SQL pod "dies" data stored on it can be lost
- storage requirements:
  - must not depend on pod life cycle
  - must be available on all nodes
  - storage must survive even if entire cluster crashes
- another application for persistent storage is read/write files to a directory
- persistent volume: cluster resource (like ram or CPU) that is used to store data
  - created using yaml file
  - is just an abstraction, so needs a physical storage as well
  - persistent volume is the interface between physical storage and cluster
  - must manage physical (or cloud) storage yourself outside of cluter
  - not in a namespace (available to entire cluster)
  - must be in cluster before pod that depends on it is created
- for DB persistence, use remote storage
- persistent volume claim (PVC): allows an appication (pod) to claim a persistent volume (PV)
  - specifies things like which volumes to claim (based on storage size or capacity and things like access type)
  - whatever PV satisfies this criteria (or claim) will be used for application
  - must also use this PVC in that pods configuration
  - must exist in same namespace as pod using the claim
- pods -> request a volume through PV claim -> claim finds a PV in the cluster -> volume has a physicsal storage backend to create resource from -> volume is then mounted into the pod and the container
  
  
