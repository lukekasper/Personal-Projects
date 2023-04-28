// make an array of pointers to int values and char values
#include <iostream>
 
using namespace std;
const int MAX = 3;
 
int main () {
   int  var[MAX] = {10, 100, 200};
   int *ptr[MAX];
   const char *names[MAX] = { "Zara Ali", "Hina Ali", "Nuha Ali"};

   for (int i = 0; i < MAX; i++) {
      ptr[i] = &var[i]; // assign the address of integer.
   }
   
   for (int i = 0; i < MAX; i++) {
      cout << "Value of var[" << i << "] = ";
      cout << *ptr[i] << endl;

      cout << "Address of names[" << i << "] = ";
      cout << (names + i) << endl;          // prints char addresses
   }
   
   return 0;
}