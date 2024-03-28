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
