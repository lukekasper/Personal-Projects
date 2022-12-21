Testing:
- Python:
  - assert: whether a statement is true or not
    - assert function(param) == expected_value
    - if true, no output occurs
    - if not true, assert will throw an exception (AssertionError)
  - to test many test cases via a script, write .sh file
  - unittest library: built into python to run boolean checks  
  - can write these tests for our django application in tests.py file
    - django will create new database soley for testing
      1) create some sample data for testing
      2) write unit tests for corner cases using sample data
      3) python manage.py test: runs all test conditions
    - check client side response of web application:
      - c = Client()
      - save the response from querying the url
      - can check the status code and the what was passed in to the render request in the application (context)
      
- JavaScript: browser testing (selenium web driver)
  - creates a test file to write client-side unit testing of JavaScript code 
  - use of web driver to simulate user interacting with program
    - must get files uri first (see file_uri(filename) function in tests.py
      - uri is used to open/load the webpage
    - get chrome we drive: driver = webdriver.Chrome()
      - must get google chrome web driver application (seperate from google chrome itself)
    - use driver.get(file_uri("name of file")) to control webpage interaction
    - write test cases to simulate user interaction with webpage
 
 CI/CD:
 - Continuous Integration (CI): frequent merges to a git repository, automated unit testing
   - Github Actions: creates workflows to run checks anytime code is pushed to github
    - ie) is code styled well?, can run unit tests on code automatically
    - immediate feedback via github if test failed whenever code is pushed
    - YAML: file format to facilitate this type of testing (.yml, .yaml file formats)
      - written in key-value pairs
      - actions/checkout: checks out code in git repository and allows us to run programs on it
    - can see result of these "jobs" in the GitHub Actions tab (output of unit tests)
- Continuous Development (CD): short release schedules
  - there may be configuration differences between what's on your computer and what's on the server
  - operating system, version differences of software (ie python)
  - Docker: instead of just running an application on your computer, run it inside of different containers that have their own software configurations
    - can use setup instruction in docker container to ensure you are working in the same environment (as say other colleagues)
    - aids in continuous delivery, avoids headache of making sure all of the right packages are installed on the server
    - Virtual Machine (VM): runs its own virtual computer, containing its own operating system, libraries, ect
    - Docker Containers: don't have their own operating system, but docker layer keeps track of individual containers which can have their own libraries
      - More lightweight than an entire virtual machine
    - Dockerfile: setup instructions for creating a docker image
      - FROM: bases dockerfile off of existing docker file template
      - COPY: everything in app directory into docker container directory
      - WORKDIR: sets working directory
      - RUN: install requirements
      - CMD: what runs when you start up the container, each word in command is an item in a python list
    - Can run on max, windows and linux to support multiple operating systems
  - In real web applications, you want your database hosted on a seperate server (not SQLite like we have been using)
    - MySQL or PostGreSQL
    - Can have one docker container running web application and another running PostGreSQL database
    - docker-compose.yml: allows us to run seperate containers that can communicate with one another
      - each service is its own container that can be based on a docker image
      - build: use docker file in current direcotry
      - volumes: current directory should correspond to my app directory
      - docker-compose up: in terminal to start up services
  - Docker cmds:
    - docker ps: shows all docker containers that are running
    - docker exec -it "container_id" bash -l: runs a bash prompt to interact with a shell and run cmds on a container
