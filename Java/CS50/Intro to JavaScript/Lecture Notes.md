Notes:
- Javascript will allow us to write client side code
  - as oppose to the server-side code we've been writing in our Django-based web applications
  - code will run inside of user's web browser
  - computations may be faster on client side
  - pages can be much more interactive, as java allows us to manipulate the content of the webpage
- Javascript can be incorporated into a webage through a <script> tag in html structure
- Event-driven programming:
  - ie) user clicks on a button/selects from a dropdown
  - can add event listeners or handlers to run blocks of code when events happen
  - code will allow page to respond to user interactions
- document.querySelector('<element>').innerHTML = 'some text': function to search for an element on html page to manipulate it
  - innerHTML accesses html inside of <element> and updates it to 'some text'
- const: sets variable to a static value that does not change
- template literal: same as a formatted string in python, called by using `some text ${variable}`
- functional programming: functions can be assigned to variables as a value
  
Debugging:
- can access JavaScript console by right clicking browser window -> inspect -> open up Console tab
- browser runs code from top to bottom, if document.querySelector is looking for an element that is below the script line, it will return null
  - common fix is to add an event listener to entire document
  - document.addEventListener('DOMContentLoaded', function(){}); 
    - event is triggered when all events on page (all of the code) has been loaded
    - can write anonymous function with code directly in line between {}
