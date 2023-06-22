References: https://www.tutorialspoint.com/cplusplus

### Storage Class
- static: keeps local variables between function calls
  - local variables maintain their values between calls
  - for global variables, it restricts the variable's scope to within the file
- extern: used to declare a global variable or function defined in another file

### Operators
- `condition ? x : y`: if condition is true, it returns x, otherwise it returns y

### Arrays
- don't have to specify size of an array, compiler will figure that out
  - also can declare an array without specifying elements, they can be added later
- sizeof(array): reutnr the size of an array in bytes
  - to get the number of elements, use `sizeof(array) / sizeof(int)`
- for-each loop: loop through elements in an array directly
  - `for (type variableName: arrayName) {}`

### Strings
- `char someString[] = "string";`: to declare a null terminated string
- C++ also supports a string class, by adding `#include <string>`
  - `string str = "Hello";`
  - supports things like `+` and `.size()`

### Structures
- combine various related variables into a single place
- able to contain different data types
- declare: `struct {int myNum; string myString;} myStructure;`
- assing variables: `myStructure.myNum = 1`
- can also assign a single structure to multiple variables
- can name a structure and treat it as a data type
  - `struct myDataType {int a; string b;};`
  - `myDataType myVar;`: creates a variable with the myDataType structure
- typedef can be used to alias structures

### Pointers:
- `&`: denotes a variables memory address
- Pointer: variable whose value is the address of another variable
  - syntax is: <type> \*<var_name>;
- Null pointer: pointer whose address is set to 0 (not referencing anything)
  - `int  *ptr = NULL;`
  - good practice for initializing pointers
  - can check if a pointer is meant to reference a value or not with `if(ptr)`
    - avoids referencing an uninitialized pointer (whcih may hold some junk value)
- Pointer arithmetic:
  - incrementing a pointer (for an array for example) will point to the next memory location
    - this allows use of `++` operator on an array pointer to iterate tyhrough the array
  - `+` or `-` can be used to reference other addresses within an array
    - if `int *ptr = arr;`:
      - `ptr + 1 == &arr[1]`
      - `*(ptr + 1) == arr[1];`
  - pointer comparisons: can use relationsl operators to compare two pointers as long as the variables are related to one another
- arrays and pointers:
  - array names often decay to pointers, meaning `*(arr + i) == arr[i]` without the need to declare a seperate pointer for "arr"
    - there are a few cases where this is not true
  - a pointer to an array points to the address of the first element of that array
- can declare an array of pointers using: `int *ptr[MAX];`
  - each element in the array is a pointer to an int value
  - can be done for any variable type
- Pointer to a pointer: points to address of a pointer, which points to address of a variable
  - syntax: `int **var;`
- functions can take pointers as arguements
  - arrays can also be passed as parameters to function calls in place of a pointer
- pointers can also be returned from functions: `int * myFunction() {}`
  - to avoid returning the address of a local variable outside of the function, define local variable as "static"
- the "this" pointer gives an object access to all of its member functions
  -  `int compare(Box box) {return this->Volume() > box.Volume();};`: where Volume is a member function of Box
- Benefits:
  - save the memory.
  - reduce the length and complexity of a program.
  - allow the passing of arrays and strings to function more efficiently.
  - make it possible to return more than one value from the function.
  - increase the processing speed. 
  
### References:
- alias to an already existing variable
  - syntax: `int& r = x;`
- cannot have a NULL reference
- once intiialized, a reference cannot change
- must be initialized at time of declaration
- do not return a reference to a local variable (out of scope will result in compiler error)
  - instead, return a reference on a static variable

### Copy Constructor
- used to:
  - initialize one object from another of the same type
  - copy an object to pass it as an argument to a function
  - copy an object to return it from a function
- can be inefficient if copying large objects

### Static Members
- static members are shared by all objects of a class (independent of a particular object creation)
- automatically initialized to zero
- for static functions, they can be called even if no objects of that class exist
- do not have access to the "this" pointer
- they only have access to static data members, other static functions, and any other functions outside of the class

### Data Abstraction
- how to use access modifiers:
  - keep members private unless necessary to access outside of class
  - use protected for inheritance
  - use composition over inheritance when possible
    - composition is building a complex object using several smaller objects, rather than inheriting those properties from a base class
    - does not totally exclude use of inheritance, you must consider the relationship between the objects to determine which method (or both) is appropriate
- encapsulation is the process of bundling together data and the functions that utilize them within a class, and keeping that info hidden from other classes (unless necessary to share)

### Files and Streams
- use seekg or seekp to place file pointer at appropriate locations within file (see example)
- best practice is to close file after use

### Dynamic Memory
- stack: variables declared inside the funciton take up memory from the stack
- heap: unused memory that can be used to dynamically allocate when program runs
- you won't always know in advance how much memory will be needed, so you can determine this at runtime
  - this can be done using the "new" operator
- use "delete" operator once you are not in need of that memory anymore to de-allocate
  - for an array, use `delete [] pvalue;` regardless of the dimensions of the array (no need for [][])
