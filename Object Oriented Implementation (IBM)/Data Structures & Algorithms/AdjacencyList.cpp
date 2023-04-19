// weighted graph implementation using adjacency list
#include <iostream>
using namespace std;

class Node{
    public:
        int vertex;     // row number of linked list
        int weight;
        Node *next;
}

// takes array of pointers (nodes) and creates directed or undirected graph
void create(Node* head[]) {
    char ch = 'y';
    int v1, v2, choice, no, weight;
    Node* newNode;
    Node* temp;

    cout<<"0 - Directed Graph\n"
    cout<<"1 - Undrected Graph\n"
    cout<<"Enter your choice (0 or 1):\n"
    cin>>choice;
    cout<<"Enter # of edges:\n"
    cin>>no;

    for (int i=0; i<no; i++) {
        cout<<"\n Enter the starting node, ending node, and weight:\n"
        cin>>v1;
        cin>>v2;
        cin>>weight;

        // creates node and assigns vertex (row index of end node in given edge) and weight
        newNode = new Node();
        newNode->vertex = v2;
        newNode->weight = weight;
        temp = head[v1];    // set current node as the start of the edge 

        // if its NULL, set the  new node as the head of the list
        if (temp == NULL) {
            head[v1] = newNode;
        }

        // otherwise, iterate to the end of the lsit and set the new node there
        else {
            while (temp->next != NULL) {
                temp = temp->next;
            }
            temp->next = newNode;
        }

        // undirected graph, must create and assign new node for that edges ending node also (since it is symmetric)
        if (choice == 1) {
            newNode = new Node();
            newNode->vertex = v1;
            newNode->weight = weight;
            temp = head[v2];

            if (temp == NULL) {
                head[v2] = newNode;
            }
            else {
                while (temp->next != NULL) {
                    temp = temp->next;
                }
                temp->next = newNode;
            }
        }
    }
}

void display(Node* head[], int n) {
    int v;
    Node *adj;
    cout<<"Adjacency List ls:\n";
    for (v=0; v<n; v++) {
        cout<<"Head["<<v<<"]";
        adj = head[v];
        while (adj != NULL) {
            cout<<adj->vertex<<"=>weight:"<<adj->weight<<" ";
            adj = adj->next;
        }
        cout<<"\n"
    }
}

int main() {
    char c = 'y';
    int n, v;
    Node *head[50];
    cout<<"No. of vertices in the graph:\n";
    cin>>n;
    for (v=0; v<n; v++) {
        head[v] = NULL;
    }
    create(head);
    display(head,n);
}