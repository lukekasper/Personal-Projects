General Notes:
- to run python program from terminal: python <file.py>
- no need to define variable type in python
- indentation is required to parse python code
- elif is used for elseif


Exceptions:
- TypeError: mismatch of types, python expects one variable type but got another
- NameError: name or function is not defined
- use try/except to catch and handle errors
    - use sys.exit(1) to exit program with status code 1


Built-in Functions:
- input("propmt:"): prompts user for input that can be stored as a variable
- print(f"Hello, {name}"): formatted string, can plug in variable value or expression into string
- append: names.append adds name to list of names
- sort: names.sort sorts list (alphabetically or numerically)
    - to perscribe how to sort data structure, use sort(key=f) where f is a function telling which variable to sort on
- len(sequence): number of elements in a sequence
- range(x): gets range of numbers up to "x" elements
    - useful for running loops


Python Sequences (very powerful aspect of Python):
- can nest data structures
- string: array of chars
- list []: of strings or variables, or other lists
    - good for elements that need to be in a particular order
- tuple (): set of 2 or more variables grouped together
    - coordinate = (10,20)
    - immutable values: cannot change values or add elements
- set {}: collection of unique values
    - s = set(): creates an empty set
    - s.add(1) adds to set; s.remove(1) removes from set
    - good for elements that are unique
- dict: collection of key-value pairs


Functions:
- can import function from other python modules
    - import square from functions: import funciton "square" from another module "function"
    - can also do import functions to import entire module
        - must call functions.square to use "square" function
- decorator: takes function as input and returns modified version of that function as an output
    - includes a wrapper function that modifies original function
    - use "@" to call decorator above function to add additional modifications
- can use a lambda funciton as shorthand for one line functions
        
        
Object Oriented Programming:
- objects store information (data) and support ability to perform operations
- class: template for a type of object
