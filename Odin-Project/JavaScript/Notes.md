## Function vs Method Invocation
- Invocation is the process of evaluating a funciton body by calling it
- A function invocation is defined by a name and arguments passed through parentheses: parseInt(23)
- A method is invoked through a property accessor: obj.myFunc()

## Scoping
- "var" scopes variables within a function
- "let" and "const" block scope variables
  - variables are scoped to the nearest {}, this can be within if statements or for loops
- A closure refers to the combination of a function and the surrounding state in which the function was declared
  - Also called its lexical environment, consists of any local variables that were in scope at the time the closure was made
- Encapsulation: bundling data, code, or something into a single unit, with selective access to the things inside that unit itself
 - Encapsulation helps avoid namespace collisions in the program
 - By putting all operator functions in a 'calculator' module, we can group them together and avoid similarly named operations that may be for string datatypes elsewhere in the program

## Modules
- Bundlers are used to combine many files into a single one at runtime in order to increase efficiency
  - It is useful for organization purposes to break code into digestable modules
  - Many files though, can lead to costly HTTP requests as the client must make requests to each individual module
- Webpack is a commonly used JavaScript bundler
  - https://webpack.js.org/guides/getting-started/
  - Given an entry point file, it will make a dependency graph starting there and bundle all imports/exports into a single file
  - This can be done for multiple entry points if there is a need for seperate bundles for different html pages
  - Webpack also supports bundling front-end support files like css, images, and data files
- Imports and Exports from JS modules: https://www.theodinproject.com/lessons/node-path-javascript-es6-modules#webpack-and-bundlers
- Babel is a transpiler, which translates stuff like more modern JavaScript code into JavaScript code that is readable by the browsers

## OOP Principals
- Single responsibility: a class should only have one responsibility
  - It can do more than one thing, but all methods and structures should relate to that purpose
  - It can call other functionality, but not define it within the class structure
  - A good example of this is that DOM manipulation should be handled in a seperate module from application logic
  - A function responbsible for the game loop can call two seperate fuctions contained in distinct modules:
    - One to check if the game is over, and another to manipulate the DOM based on the bool return value
  - Loosely coupled objects: objects or classes are not heavily dependent on one another
    - Game logic should not depend on the user interface.  We can start writing the game logic using console.log() statements and later add the UI without affecting the game logic
    - Publish/Subscribe relationships can incorporate a "mediator" class to facilitate communication and loose coupling
      - JavaScript has a pub/sub library called PubSubJS
- Open/Closed Principal: open for extension, closed for modification
  - Means we should be able to add new types to a class from outside without needing to change the code inside the class explicitly
  - Usually switch statements or multiple if statements are clues that Open/Closed Principal is being violated
  - In print quiz example (https://www.youtube.com/watch?v=-ptMtJAdj40&list=PLZlA0Gpn_vH9kocFX7R7BAe_CvvOCO_p9&index=2):
    - Rather than check for a question type in the printQuiz method and then follow the conditional tree to the appropriate print statement
      - This would force a new conditional every time we make a new question type
    - We can make a class for each type, and the class will know how to print itself calling a common printQuestionChoices method
      - Then from printQuiz, we just call the the generic print method, which will refer to the appropriate question type based on how the question object was created
      - The type is defined outside of these methods by creating unique question objects for each question type (corresponding to our question type classes)
    - This allows us to extend printQuiz by adding additional question types, while allowing it to remain closed to modification (no edits are necessary to this method to extend functionality)
- Liskov Substitution Principal: a parent class should be replacable by any of its subtypes
- Integration Segregation Principal: when a class implements an interface, it must use every functionality of that interface
  - If a class does not need all of the methods/attributes of an interface, the interface should be sub-divided into more modular pieces
  - JavaScript can just use classes rather than interfaces to accomplish this, still requires breaking class into modular components
  - Create javascript component objects that contain relevant methods, and then use Object.assign(<Class>.prototype, <component>) to assign necessary functionality to each class instance
- Dependency Inversion: create a wrapper or intermediary abstract class that facilitates API calls to the dependencies
  - This makes our high-level code only dependent on the wrapper and not the low-level dependency implementations explicitly
  - Can just make a new wrapper class for additional API needs rather than modify the high-level code

 ## Linting with JavaScript
 - Style guide: https://github.com/airbnb/javascript
 - Linters: https://eslint.org/
 - Automatic styling with Prettier: https://prettier.io/
 - Using Prettier and ESLint together: https://github.com/prettier/eslint-config-prettier#installation
 - GitHub offers repository templates to expedite setup
   - Any repository can be marked as a template and reused in future new projects as a starting point
  
## Client-Side Form Validation
- Accomplished in two ways: with built-in HTML form validation or with customizeable JavaScript
  - Built-in validation can set parameters like: required, min/max length, min/max, type, regex pattern match
  - `:valid` css pseudo-class allows specific styling to be applied to valid elements (same goes for `:invalid`)
  - JavaScript is necessary to take control of the error messages
    - https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation#validating_forms_using_javascript
    - https://www.w3schools.com/js/js_validation_api.asp

## Asynchronous Code
- Functions that happen in the background while the rest of your code executes
- Callback: a function that is passed into another function as an argument and invoked within that outer function
  - Most commonly an event listner pattern, which takes an anonymous function as input and executes it when the event is triggered
  - Also common to use asynchronous functions for file/harddrive read operations or API calls to fetch data
- Promise: an object that might produce a value at some point in the future
  - Most commonly used with the "fetch" api
  - Must call 'resolve' or 'reject' methods based on the result of the given task
  - .then: used to react to the promise, recieving the 'result' from the resolve method
  - .catch callback is executed when the promise is rejected (like sending an error to print or be displayed)
  - .finally is called regardless of success or failure
  - Promise.all is used when you want to respond only when a series of asynchronous calls have completed
  - Promise.race is used to fire a callback whenever the first promise is resolved or rejected
    - Could be used to query an API for a primary and secondary source and respond to the first available data

## Event Loop
- The stack is synchronous code waiting to be executed
- Event loop in JavaScript is how asynchronous code gets executed in the browser
- Callback queue is where the asynchronous calls are stored prior to being executed in the call stack
  - The event loop will only push an event from the callback queue to the call stack if the call stack is empty
- Likewise, the Render Queue (when the browser will render display changes) is only able to update when the call stack is empty
  - When someone says "don't block the stack", they mean don't clog up the call stack with slow-executing code which prevents callbacks from executing and display changes rendering
- You can also flood the callback queue by including events that are constantly being triggered (like a general "on scroll")

## APIs
- Servers that are created for serving data for external use
- The "fetch" and "catch" methods (illustrated in my Recipes project) are the most common ways of accessing API info
  - May need to configure Cross Origin Resource Sharing (CORS) to make HTTP requests to outside sources
  - Fetch methods will return a promise, so to access the underlying data, you will need to run a seocnd .then() call on response.json()
  - The response.json() line converts the promise into a json object
- Public APIs: https://github.com/n0shake/Public-APIs
- Examples of fetch requests using await: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
- Async/await methodology is preferreed to .then() calls due to the better readability and ability to handle all errors inside of a try-catch block around the entire
  - Can pair await with Promise.all([]) to fire multiple async calls concurrently and wait to process until the last one is complete
- Also standard practice to create a higher-order error handler that takes in the unsafe function and adds on a .catch() statement to handle the error
  - Better practice because it allows you to write routes without worrying about error handling, and just wrap route in the same error handler class
- Unhandled rejected promises can be handled at the global scope with the event listener "unhandledrejection"

## Space/Time Complexity Cheat Sheet
- https://www.bigocheatsheet.com/
- Code for readability first, unless there is a noticeable impact to performance

## Unit Testing
- Jest is the most commonly used JavaScript TestRunner
  - Can configure it to run on each save, to ensure code logic is sound right in the IDE
  - Use "watch: jest --watch *.js" in package.json file and run `npm run watch` in command line
  - https://jestjs.io/docs/using-matchers
  - Jest also offers mock testing libraries for mocking things like fetch calls
- Test Driven Development (TDD) is a dev technique that states we write a test prior writing code
  - Keeps code modularized and focused on meeting requirements, easy to know what to develop next
- Pure function:
  - The function always returns the same result if the same arguments are passed in. It does not depend on any state, or data, change during a program’s execution. It must only depend on its input arguments.
  - The function does not produce any observable side effects such as network requests, input and output devices, or data mutation.
