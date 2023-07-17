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
  - add `-p<host port>:<container port>` to bind ports
  - add `--name <container name>` to name container
- `docker ps`: list running containers
  - add `-a` to get history of running/stopped containers
- `docker stop <id>`: stop container
- `docker start <id>`: restart container
- `docker logs <id>`: print logs
  - can also use container name instead of id
- `docker exec -it <id> /bin/bash`: enter container terminal (in bash) as root user
  - able to view and navigate virtual file system in container
  - can print environmental variables, ect

### Ports
- containers have their own ports which differ from the host machine
- must bind host ports to the specified ports that the containers are set to listen to
  - container port is based on pulled image
  - without port binding, the container is unreachable
  - specify port binding during the run cmd
