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
