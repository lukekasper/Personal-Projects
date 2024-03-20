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
