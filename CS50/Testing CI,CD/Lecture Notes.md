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
- JavaScript: selenium
  - creates a test file to write client-side unit testing of JavaScript code 
  - use of web driver to simulate user interacting with program
    - must get files uri first (see file_uri(filename) function in tests.py
      - uri is used to open/load the webpage
    - get chrome we drive: driver = webdriver.Chrome()
      - must get google chrome web driver application (seperate from google chrome itself)
    - use driver.get(file_uri(<name of file>)) to control webpage interaction
    - write test cases to simulate user interaction with webpage
 
