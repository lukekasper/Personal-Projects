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
