// Linked-list implementation
#include <iostream>
using namespace std;

// class for node has a property for data and a reference to the next node
class Node {
    public:
        int data;
        Node* next;
};

class LinkedList {
    
    public:
        Node *head, *tail;  // declare attribute references for head and tail nodes
        
        // initialize member variables head and tail nodes to NULL with constructor
        LinkedList() {
            head = NULL;
            tail = NULL;
        }
    
        // member function to insert new node at beginning of list
        void insertNodeAtFront(int value) {

            // create a new node object
            Node *newNode = new Node;

            // assign its value and initialize its pointer to NULL
            newNode->data = value;
            newNode->next = NULL;

            // if the current head is NULL (list is empty), set the head and tail as the new Node (only node in list)
            if (head == NULL) {
                head = newNode;
                tail = newNode;
            }

            // otherwise reference the new node's pointer to the current head, and assign the new node as the new head
            // when a node is inserted at the beginning, only the reference to 'next' needs to be modified
            else {
                newNode->next=head;
                head=newNode;
            }
        }

        // member function to insert new node at end of list
        void insertNodeAtEnd(int value) {

            // create a new node object
            Node *newNode = new Node;

            // assign its value and initialize its pointer to NULL
            newNode->data = value;
            newNode->next = NULL;

            // if the current head is NULL (list is empty), set the head and tail as the new Node (only node in list)
            if (head == NULL) {
                head = newNode;
                tail = head;
                return;
            }

            // otherwise reference the current tail's next reference to the new node, and then update the tail object to the new node
            else {
                tail->next=newNode;
                tail=tail->next;
                return;
            }
        }

        // member function to insert new node at end of list
        void insertNodeAtPosition(int pos, int value) {

            // create a new node object for previou, current, abd new nodes and update the current node as the head
            Node *prev = new Node;
            Node *current = new Node;
            Node *newNode = new Node;
            current = head;

            // assign the new node's value and initialize its pointer to NULL
            newNode->data = value;
            newNode->next = NULL;

            if (pos < 1) {
                cout<<"Pos cannot be less than one."
            }
            // if the position is 1, update the new node's next reference to the current head object, and then update the head object to the new node
            else if (pos == 1) {
                newNode->next = head;
                head = newNode;
            }
            // otherwise loop through the list up to the pos parameter
            else {
                for (int i=1; i<pos; i++) {
                    prev = current;                 // make the previous pointer rerfernce the current object
                    current = current->next;        // update the current pointer to the next node
                    if (current == NULL) {          // if the current node now reads NULL, pos was specified outside of the list index
                        cout<<"Invalid position";
                        return;
                    }
                }

                // once the pos in the list is reached:
                prev->next=newNode;                 // set the previous node's pointer to the new node
                newNode->next=current;              // and set the new node's next pointer to next node in the list (current object)
            }
        }

        // search and display elements in the list
        void search(int value) {
            Node *current = head;       // create reference variable 'current' and store the head object in it
            while (current != NULL) {
                if (current->data == value) {
                    cout<<"Element"<<value<<" is found";
                    return;
                }
            }
            cout<<"Element"<<value<<" not found";
        }

        void displayList() {
            Node *current = head;
            while (current != NULL) {
                cout<<current->data<<" ";
                current = current->next;
            }
        }

        // delete a node from the list
        void deleteNode(int value) {

            // set flag and create new node objects for current and preivous pointers; set both to the head object
            bool flag = false;
            Node *current = new Node;
            Node *previous = new Node;
            previous = head;
            current = head;

            // loop over the list
            while (current != NULL) {

                // if the current node has that value and its the head
                if (current->data == value and current == head) {
                    head = current->next;               // set the head object to the next node
                    free(current);                      // delete that node
                    flag = true;
                    break;
                }

                // if the current node has that value and is not the head
                else if (current->data == value) {
                    previous->next = current->next;     // re-reference the current and previous pointers forward one node
                    if (current == tail) {
                        tail = previous;                // if the current node is now the tail, re-reference the tail to the previous node
                    }
                    free(current);                      // delete that node
                    flag = true;
                    break;
                }

                // otherwise re-reference the previous and current pointers forward one node
                else {
                    previous = current;
                    current = current->next;
                }
            }

            // print whether the element was deleted or not based on the flag
            if (flag == true) {
                cout<<"Element deleted";
            }
            else {
                cout<<"Element not found";

            }
        }
};  // linked list ends here

int main() {
    LinkedList lst;
    lst.insertNodeAtFront(10);
    lst.insertNodeAtEnd(40);
    lst.insertNodeAtEnd(50);
    lst.insertNodeAtPosition(2,20);
    lst.insertNodeAtPosition(3,30);
    lst.search(30);
    lst.deleteNode(30);
    lst.displayList();
    return 0;
}
