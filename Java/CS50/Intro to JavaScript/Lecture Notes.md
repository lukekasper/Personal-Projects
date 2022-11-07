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
  
Query Selector:
- document.querySelector('<element>').innerHTML = 'some text': function to search for an element on html page to manipulate it
  - innerHTML accesses html inside of <element> and updates it to 'some text'
- functional programming: functions can be assigned to variables as a value
- query selector can call elements same way as css (ie '.class' or '#id')
- can use document.querySelector().style to change page's css
- can add data attributes to html elements with: data-color="red" for example
- querySelectorAll returns array of all elements that match this criteria
- events: onclick, onmouseover, onkeydown (when you press down on a key), onkeyup, onload, onblur...
  
Debugging:
- can access JavaScript console by right clicking browser window -> inspect -> open up Console tab
  - console is like the terminal window but interacts with html on webpage
- browser runs code from top to bottom, if document.querySelector is looking for an element that is below the script line, it will return null
  - common fix is to add an event listener to entire document
  - document.addEventListener('DOMContentLoaded', function(){}); 
    - event is triggered when all events on page (all of the code) has been loaded
    - can write anonymous function with code directly in line between {}
- can also write javascript code in console

General JavaScript Notes:
- const: sets variable to a static value that does not change
- template literal: same as a formatted string in python, called by using `some text ${variable}`
- autofocus tag on html form focuses page on that form
- arrow notation: () => can take the place of a function()
- "this": special keyword that refers to the thing that recieved the event (for eventListener)
- setInterval: builtin javascript function that runs every x milliseconds
- local storage: saves users information in a browser:
  - localStorage.getItem() and localStorage.setItem()
  - can view value of local storage in Inspector under Application tab -> Local Storage
- JavaScript object: like a python dictionary 

APIs:
- a way to communicate with other services by sending requests and recieving back data in a well structured format
  - json: javascript object notation
  - a way of transferring data in the form of javascript object
- companies often offer API services in the form of json objects to acces certain information
- Ajax: asynchronous javascript
  - fetch: makes a web request to get an httpresponse (can be used to get API info)
- .serialize() creates a URL encoded text string by serializing form values, used to export as json objects 
