### Arrays
- don't have to specify size of an array, compiler will figure that out
  - also can declare an array without specifying elements, they can be added later
- sizeof(array): reutnr the size of an array in bytes
  - to get the number of elements, use `sizeof(array) / sizeof(int)`
- for-each loop: loop through elements in an array directly
  - `for (type variableName: arrayName) {}`

### Structures
- combine various related variables into a single place
- able to contain different data types
- declare: `struct {int myNum; string myString;} myStructure;`
- assing variables: `myStructure.myNum = 1`
- can also assign a single structure to multiple variables
- can name a structure and treat it as a data type
  - `struct myDataType {int a; string b;};`
  - `myDataType myVar;`: creates a variable with the myDataType structure

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
  
### References:
- alias to an already existing variable
  - syntax: `int& r = x;`
- cannot have a NULL reference
- once intiialized, a reference cannot change
- must be initialized at time of declaration
- do not return a reference to a local variable (out of scope will result in compiler error)
  - instead, return a reference on a static variable
