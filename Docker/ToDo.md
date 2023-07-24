Docker Containerization ToDo list:
- update requirements.txt to include all app dependencies
  - check for installations using `pip list`
- save the AppleScript code as an application:
  - Click on "File" in the menu bar, then select "Save..."
  - Choose a location to save the application.
  - Set "File Format" to "Application" (this is important).
  - Give the application a name (e.g., "Start My App").
  - Click "Save."

General ToDos:
- Finish up features and bug fixes on development side
- Add in error handling on front and backend using:
  - back end:
    - `if request.method == 'POST':`
      - `return JsonResponse({'error': 'Invalid request method.'}, status=400)` or something similar
      - `return JsonResponse({'message': 'Data received successfully.'})` if it is a post request and nothing else is returned
    - additional try and catch/throw error blocks where applicable for data processing
  - front end:
    - `.catch(error => {// Handle errors});`: after fetch request in case error message is returned from back end
- Security concerns:
  - added env variables and SECRET key for database and django app (done)
  - include csrf tokens on front end requests
  - look into secure file uploads for images
  - re-watch CS50 security lesson
- Testing and Deployment:
  - add in rudimentary unittesting for front/back end
  - create CI pipeline for automated testing and containerized deployment through github

Additional tasks:
- use black linting code for formatting
- integration tests for interaction between app add db?
- seperate github action workflows for ci and cd
- consider deploying on a cloud environment
