/* program will terminate on the 4th iteration or if it recieves the ctrl+c terminate cmd line command
   without interference, the program will automatically produce:
     Going to sleep....
     Going to sleep....
     Going to sleep....
     Interrupt signal (2) received.*/
#include <iostream>
#include <csignal>

using namespace std;

void signalHandler( int signum ) {
   cout << "Interrupt signal (" << signum << ") received.\n";

   // cleanup and close up stuff here  
   // terminate program  

   exit(signum);  
}

int main () {
   int i = 0;
   // register signal SIGINT and signal handler  
   signal(SIGINT, signalHandler);  

   while(++i) {
      cout << "Going to sleep...." << endl;
      if( i == 3 ) {
         raise( SIGINT);
      }
      sleep(1);
   }

   return 0;
}