// Increment array using pointer
#include <iostream>

using namespace std;
const int MAX = 3;

int main () {
   int  var[MAX] = {10, 100, 200};
   int  *ptr;

   // let us have address of the first element in pointer.
   ptr = var;       // same as &var[0]
   int i = 0;
   
   // increment while the pointer address is <= the address of the last item in the array
   while ( ptr <= &var[MAX - 1] ) {
      cout << "Address of var[" << i << "] = ";
      cout << ptr << endl;

      cout << "Value of var[" << i << "] = ";
      cout << *ptr << endl;

      // point to the next location
      ptr++;
      i++;
   }
   
   return 0;