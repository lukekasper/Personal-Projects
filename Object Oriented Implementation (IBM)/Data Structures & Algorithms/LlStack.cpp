#include <iostream>
using namespace std;

class Node {
    public:
        int data;
        Node *next;
};

class Stack {
    public:
        Node *top;  // declare top pointer
        
        // constructor to initialize top to NULL
        Stack() {
            top = NULL;
        }

        // declare member functions
        void push(int n);
        void pop();
        int peak();
        void display();
};

// push an item to the top of the stack
void Stack::push(int n) {

    // create a newNode for the item and initialize it to the provided parameter
    Node *newNode = new Node();
    newNode->data=n;

    // if the stack is empty, define the node's next reference to NULL (only item in stack)
    if (top == NULL) {
        newNode->next = NULL;
    }

    // otherwise, the next reference for the new node was the previous top node in the stack
    else {
        newNode->next = top;
    }
    top = newNode;      // re-reference the top variable to the new node
}

void Stack::pop() {
    Node* temp;
    if (top == NULL) {
        cout<<"Stack Underflow"<<endl;
        return;
    }

    // assign the temp node as the top variable, re-reference the top variable to the next node, then delete the temp variable (previous top of stack)
    temp=top;
    top=top->next;
    delete temp;
}

// return top of stack
void Stack::peek() {
    if (top == NULL) {
        cout<<"\nStack underflow";
        return -1;
    }
    return top->data
}


// display the full stack
void Stack::display() {
    Node* temp;
    if (top == NULL) {
        cout<<"\nStack underflow";
        return -1;
    }
    else {
        temp = top;
        while (temp != NULL) {
            cout<<temp->data<<" ";
            temp = temp->next;
        }
    }
}