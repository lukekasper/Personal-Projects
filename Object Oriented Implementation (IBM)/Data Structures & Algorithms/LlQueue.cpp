// Queue implementation with linked-list
#include <iostream>
using namespace std;

class Node {
    public:
        int data;
        Node *next;
};

class Queue {
    public:
        Node *front, *rear;  // declare front/rear pointers
        
        // constructor to initialize variables to NULL
        Queue() {
            front = rear = NULL;
        }

        // declare member functions
        void enQueue(int n);
        void deQueue();
        void display();
};

void Queue::enQueue(int n) {
    Node *newNode = new Node();
    newNode->data=n;
    newNode->next = NULL;

    if (front == NULL && rear == NULL) {
        front = rear = newNode;
    }

    else {
        rear->next = newNode;
        rear = newNode;
    }
    cout<<n<<" Element inserted"<<endl;
}

void Queue::deQueue() {

    if (front == NULL && rear == NULL) {
        cout<<"Stack underflow"<<endl;
        return 0;
    }

    Node *temp = front;
    else if (front == rear) {
        front = rear = NULL;
    }

    else {
        front = front->next;
    }
    cout<<temp->data<<" Element deleted "<<endl;
    delete temp;
}

void Queue::display() {
    if (front == NULL) {
        cout<<"Queue Empty"<<endl;
    }
    else {
        Node *temp = front;
        while (temp != NULL) {
            cout<<temp->data<<" "<<endl;
            temp = temp->next;
        }
    }
}