reference: https://www.youtube.com/watch?v=3c-iBn73dDE

### Overview
- container: way to package an application with all necessary dependencies and configurations
  - package is portable
  - makes development and deployment more efficient
- container repository: special type of storage for containers
  - Docker Hub is a public repository for Docker containers for any application image
- application development:
  - containers remove the need to install dependent services (PostgresSQL, Django, ect) directly on your OS
  - is its own isolated OS environment layer
  - only one docker cmd is necessary to download and start docker application
- application deployment:
  - developers and operations teams work together to package application in container
  - no environmental configuration needed on server (except Docker runtime)
  - all that is necessary is to run a Docker cmd to pull the Docker image and then run it
    - all other dependency info is contained within the image
- containers:
  - layers of images
  - base is usually a linux base image (alpine)
  - application image on top (postgres)
- image vs container:
  - image: the actual package (application, configuration, dependencies, ect)
    - moveable artifact
  - container: when you pull the image and actually start the application
    - container environment is created

### Docker vs Virtual Machine
- OS systems have two layers: kernel and application layers
  - kernel communicates with hardware (CPU, RAM, ect)
  - applications run on kernel layer
- Application virtualization is a process that deceives a standard app into believing that it interfaces directly with an operating system's capacities when, in fact, it does not
- Docker virtualizes application layer
  - uses host OS kernel
- VM virtualizes both application and kernel layers
  - when you download VM image, it uses its own kernel (not the OS of the host)
- Consequences of this
  - Docker image is much smaller and start/run much faster
  - Compatibility: VM of any OS can run on any OS host
    - not true with Docker

### Basic Commands
- `docker pull <image name>`: pull docker image from url
- `docker run <image name>`: start up container from pulled image
  - add `-d` before image name to run in detatched mode and allow command line access
  - add `-p <host port>:<container port>` to bind ports
  - add `--name <container name>` to name container
- `docker ps`: list running containers
  - add `-a` to get history of running/stopped containers
- `docker stop <id>`: stop container
- `docker start <id>`: restart stopped container
- `docker logs <id>`: print logs
  - can also use container name instead of id
- `docker exec -it <id or name> /bin/bash`: enter container terminal (in bash) as root user
  - able to view and navigate virtual file system in container
  - can print environmental variables, ect
  - some containers may not have bash installed, use sh instead
  - `exit` to leave terminal

### Ports
- containers have their own ports which differ from the host machine
- must bind host ports to the specified ports that the containers are set to listen to
  - container port is based on pulled image
  - without port binding, the container is unreachable
  - specify port binding during the run cmd

### Workflow with Docker
<img width="1259" alt="Screen Shot 2023-07-18 at 3 11 17 PM" src="https://github.com/lukekasper/Personal-Projects/assets/28813582/606653e3-517f-4b97-b0ae-c3e4c86a9864">

### Docker Network (example at 01:15:00)
- when Docker containers started, they run on an isolated Docker network
- can connect containers within this network using just the container names because they are in the same network
- applications running outside of this Docker network can connect using "localhost:<port number>"
- `docker network create <network name>`: to create a new network connection
- when running the container image, must supply:
  - port of the host and container using `-p <host:container port>`
  - environmental variables (suggested on Docker Hub) using `-e <env variable=value>`
  - container name using `--name <container name>`
  - network using `--net <network name>`

### Docker Compose
- way to automate running multiple containers with configurations
  - structured in a yaml configuration file
- when you restart a container, everything configured within that container is reset
  - no data persistence
- `docker-compose -f <yaml name> up -d`: start all containers in yaml file
- `docker-compose -f <yaml name> down`: stop all containers in yaml file
  - also removes the network
 
### Dockerfile
- to deploy, application must be packaged into its own container
  - ie from a javascript node js application
- Jenkins automates this functionality and pushes it to a Docker repository
- Dockerfile: blueprint for building images
- base application image on some known image as a starting point
  - for our application use node js image as a starting point since that makes up the backend
  - will automatically have node installed in image
- can configure environemntal variables in Dockerfile
  - probably better to do this in Docker-Compose
  - if something changes you can override it in Docker-Compose rather than needing to rebuild the image
- Use "RUN" to create directory inside of the container, not on host computer
  - RUN allows execution of any linux commands in container environment
- COPY command executes on the host machine
  - `COPY <source> <target>`
- CMD executes an entrypoint linux cmd
  - `CMD ["node","server.js"]`
  - runs commands within the brackets
  - since CMD is entrypoint, can only contain one within Dockerfile
    - runs the server and thats it
- Dockerfile is part of application code just like Docker-Compose
- Dockerfile must be named "Dockerfile" exactly
- to build an image using a Dockerfile:
  - `docker build -t <image name>:<tag> <location of Dockerfile>`
- in order to use Jenkins:
  - must commit this Dockerfile to the repository along with the code
  - Jenkins or Github will then create an image from this Dockerfile
  - in a development team, this image would then be pushed to a Docker repository for dev teams to checkout and test
- whenver you adjust a Dockerfile, you must rebuild the image
  - `docker rmi <id>`: delete an image
  - `docker rm <id>`: delete a container
  - cannot delete an image if a stopped container is using that image, must remove container first
- in a typical application with a lot of files, you would want to compress these into a singular artifact and copy that into a Docker image container

### Docker Registry
- private Docker repository (on AWS ECR for example)
- each Docker image has its own repository (specific to AWS)
  - within this repository are different tags (or versions) of the same image
  - to push to repository:
    - must login to private repo
      - if it is pushed from a Jenkins server, you must give Jenkins the credentials of the private repo in order to push a Docker image
    - must tag image
      - image naming in Docker registries: <registryDomain>/<imageName>:<tag>
      - tagging image adds information about the private repo to the image name to let docker know where to push the image
      - `docker tag <app_name>:<version> <registryName>`

### Deploy Containerized App
- to pull container from private Docker repo, dev server must have login info
  - not necessary for public Docker Hub images
- include the repository domain in the docker-compose file in order to start application along with other accompanying containers

### Persisting Data with Volumes
- data is stored within a container typically in the virtual file system
  - when the container is restarted, the file system is as well and the data is lost
- docker Volumes:
  - host file system (physical) is mounted into the virtual file system of Docker
  - data gets automatically replicated into the host file system
- types of Volumes:
  - Host Volume: 
    - `docker run -v <host directory>:<container directory>` to assign the storage pathway
    - you decide where on the host side the file system reference is made
  - Anonymous Volume:
    - `docker run -v <container directory>`: automatically generates a folder at "/var/lib/volumes/…" on the host machine that gets mounted to the container
  - Named Volume: 
    - `docker run -v <name>:<container directory>`: can reference this volume by name
    - typically used in production environments
- volume creation can also be done using Docker-compose
- can mount the same host storage to multiple containers
  - useful if containers need to share data
- when setting up volumes in Docker-compose, you must figure out what path the database type stores the data within the container folder hierarchy
  - different for each db type (Postgres, Mysql, ect), can be found through google search
- Docker volumes on mac: "/var/lib/docker/volumes"
  - Mac OS actually creates a linux VM to store the volume data
  - folder location won't be available at the above pathway
