#include <iostream>
#include <cstdlib>
#include <pthread.h>

using namespace std;

#define NUM_THREADS 5

struct thread_data {
   int  thread_id;
   char *message;
};

void *PrintHello(void *threadarg) {
   struct thread_data *my_data;                 // declare pointer "my_data" of type "struct thread_data"
   my_data = (struct thread_data *) threadarg;  // assign pointer value of threadarg;  () are necessary to group together the type cast for "threadarg"

   cout << "Thread ID : " << my_data->thread_id ;
   cout << " Message : " << my_data->message << endl;

   pthread_exit(NULL);
}

int main () {
   pthread_t threads[NUM_THREADS];      // create 5 thread objects
   struct thread_data td[NUM_THREADS];
   int rc;
   int i;

   for( i = 0; i < NUM_THREADS; i++ ) {
      cout <<"main() : creating thread, " << i << endl;

      // assign data to td objects (which are thread_data structures)
      td[i].thread_id = i;
      td[i].message = "This is message";

      // create each thread, using the thread object and the td object to pass arguements to each thread
      rc = pthread_create(&threads[i], NULL, PrintHello, (void *)&td[i]);
      
      if (rc) {
         cout << "Error:unable to create thread," << rc << endl;
         exit(-1);
      }
   }
   pthread_exit(NULL);
}