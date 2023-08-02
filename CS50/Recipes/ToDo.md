Docker Containerization ToDo list:

    save the AppleScript code as an application:
        Click on "File" in the menu bar, then select "Save..."
        Choose a location to save the application.
        Set "File Format" to "Application" (this is important).
        Give the application a name (e.g., "Start My App").
        Click "Save."

General ToDos:
- Finish up features and bug fixes on development side
- Security concerns:
  - look into secure file uploads for images
  - re-watch CS50 security lesson
- Testing and Deployment:
  - add in rudimentary unittesting for front/back end
  - create CI pipeline for automated testing and containerized deployment through github (ci)
  - create automated database migration scripts (cd)
      - use python manage.py makemigrations and python manage.py migrate in automated deployment process
- Implement client-side and server-side caching
    - clear cache when updating a recipe!
- Use "black" linting code for formatting
- Integration tests for interaction between app add db?
- Seperate github action workflows for ci and cd
- Consider deploying on a cloud environment using kubernetes
- Conduct security audit using github actions
- Documentation on setup, app usage, troubleshooting, ect.
    - Comprehensive ReadMe.
- Re-implement some of the front end using React.js

## Overview of Application
- Front End:
    - Javascript to dynamically display front end
        - React framework (to do)
    - HTML/CSS
        - Bootstrap/Flexbox
- Back End:
    - Python/Django Framework
    - MySQL db
- Testing & CI/CD:
    - Unit testing with pytest (to do)
    - Integration tests for interaction between app add db?
    - CI pipeline to automate testing (to do)
    - CD pipeline to automate containerization and db migrations (to do)
- Caching:
    - Implementation of front end/back end caching using Django framework (memcached on local host)
    - Could extend to Redis db?
- Security:
    - CSRF tokens sent from front end during API calls
    - Error handling:
        - Back end: try/except statements used for every view to account for improper request methods or JSON data
        - Front end: try/catch methods used to catch network or response errors from back end and display error message to user
    - Environmental variables loaded through secret .env file kept offline from repository to enhance security
    - Security for image uploads? (to do)
    - Conduct security audit using github actions (to do)
- Deployment:
    - Custom docker image used to build application container
    - DockerHub off-the-shelf image used for mySQL db
    - Docker-compose used to build and run containers and creat network for db/app communication
    - Requirements.txt file used to supply db/app dependencies
    - Volumes persisted on local machine (for now)
    - Startup script used to install docker/docker-compose on host machine and run docker-compose.yaml file
    - Made specifically for MacOS
    - Consider deploying on a cloud environment using kubernetes
- Documentation/Formatting:
    - Docstrings/comments supplied for python back end
    - Comprehensive ReadMe for application overview, setup instructions, and troubleshooting (to do)
    - "Black" used for code linting
