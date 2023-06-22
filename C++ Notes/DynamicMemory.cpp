#include <iostream>
using namespace std;

class Box {
   public:
      Box() { 
         cout << "Constructor called!" <<endl; 
      }
      ~Box() { 
         cout << "Destructor called!" <<endl; 
      }
};
int main() {
   Box* myBoxArray = new Box[4]; // allocate memory for an array of 4 box objects
   delete [] myBoxArray; // Delete array

   return 0;
}