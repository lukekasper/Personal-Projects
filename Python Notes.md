### Arrays: 
- https://www.studytonight.com/post/list-slicing-in-python-with-examples
- eval(): mathematically evaluates a string expression
- count = collections.Counter(s): gives back a dictionary with word occurences count (must "import collectoins" library)
- for idx, ch in enumerate(s): steps through an array 's' using variable 'ch', and tracks the index of that array element using 'idx'
- all(): returns true if all objects in an interable are true, otherwise returns false (returns true if object is empty also)
- remove(element): removes the specified element from the list
- pop(): removes an array element at specified index and returns removed element
- append(element): appends an element to the end of a list
- extend(elements): appends multiple elements to the end of the list
- insert(yi,y): inserts element at the specified index within a list
- replace(oldvalue, newvalue, count): replaces a specified phrace with a new phrase
- s.sort(): sorts a list, does not return anything
  - optional arguements to reverse sort or provide a key (function) to specifiy sort criteria
- sorted(s): can be used to sort a string, list, set, dict, ect
  - returns a list of sorted items
- sum(array): sums array elements

- sets:
  - intersection() or '&': returns element in common between two sets
  - symmetric_difference() or '^': set of elements in only one of the two sets
  - "s1 - s2": set of elements in s1 but not s2
  - union() or |: combines two sets

- dictionary.items():
  - returns an object containing key-value pairs as tuples in a list


## Advanced Python Concepts
#### Tuple Unpacking + Tuple Unpacking With *:
- `person = ['bob', 30, 'male']`
  `name, age, gender = person`  
  `# name='bob, age=30, gender='male'`  
  
- `fruits = ['apple', 'orange', 'pear', 'pineapple', 'durian', 'banana']`  
  `first, second, *others = fruits`  
  `# first='apple', second='orange'`  
  `# others = ['pear', 'pineapple', 'durian', 'banana']`  

#### List Comprehension: make a list (or dictionary/set) in one line of code
- `l4 = [i for i in range(1,5) if i%2==1]   # [1,3,5]`
- `d1 = {i:i**2 for i in range(1,4)}        # {1:1, 2:4, 3:9}`  

#### Combine conditionals into a single line using ternary operator
- `score = 57`  
  `grade = 'A*' if score>90 else 'pass' if score>50 else 'fail'`  
  `# grade = 'pass'`

#### Magic methods for python classes:
- `def __str__(self)`: returns specified string when you print the class object
- `def __gt__(self, otherDog)`: provides guidance on how to compare two class objects

#### args & kwargs
`*args`: pass as a paramater to a function to allow funcitons to take any number of positional arguements
  - will be stored in as a tuple in "args"

`**kwargs`: pass as a paramater to a function to allow funcitons to take any number of keyword arguements
  - will be stored in as a dict in "kwargs"  


