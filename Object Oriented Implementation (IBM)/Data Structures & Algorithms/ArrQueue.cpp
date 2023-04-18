// Implementation of queue using array
#include <iostream>
using namespace std;
#define MAX 10

class Queue {
    int front, rear;
    public:
        int arr[MAX];           // array size

        // constructor to initialize front and rear variables
        Queue() {
            front = rear = -1;
        }

        // declare enQueue and deQueue member functions for outside definition
        void enQueue(int item);    
        int deQueue();
};

void Queue::enQueue(int item) {
    if (rear == MAX-1) {
        cout<<"\nQueue overflow";
    }

    // if queue is empty, set front and rear to the first index, and insert the item there
    else if (front == -1 && rear == -1) {
        front = rear = 0;
        arr[rear] = item;
        cout<<"\Item inserted "<<item;

    }

    // otherwise, incrememnt the rear and insert the item there (front remains the same)
    else {
        rear++;
        arr[rear] = item;
        cout<<"\Item inserted "<<item;
    }
}

void Queue::deQueue() {
    if (rear == -1) {
        cout<<"\nQueue underflow";
    }

    else {
        item = arr[front];
        
        // if only one item is in the array, set front and rear = -1 (empty)
        if (front == rear) {
            front = rear = -1;
        }

        // otherwise, move front to next element in the queue (rear remains the same)
        else {
            front++;
            cout<<"\Item deleted "<<item;
        }
    }
}