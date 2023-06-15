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

