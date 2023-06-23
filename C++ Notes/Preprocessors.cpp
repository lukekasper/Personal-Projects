// runs in debug mode and comments out part of code
#include <iostream>
using namespace std;
#define DEBUG  // signifies processor to run in debug mode

#define MIN(a,b) (((a)<(b)) ? a : b)

int main () {
   int i, j;
   
   i = 100;
   j = 30;

#ifdef DEBUG
   cerr <<"Trace: Inside main function" << endl;
#endif

#if 0
   /* This is commented part */
   cout << MKSTR(HELLO C++) << endl;
#endif

   cout <<"The minimum is " << MIN(i, j) << endl;

#ifdef DEBUG
   cerr <<"Trace: Coming out of main function" << endl;
#endif

   return 0;
}

// use of # operator, returns "HELLO C++"
#define MKSTR( x ) #x

int main () {

   cout << MKSTR(HELLO C++) << endl;

   return 0;
}

// use of ## operator, returns 100
#define concat(a, b) a ## b
int main() {
   int xy = 100;
   
   cout << concat(x, y);
   return 0;
}