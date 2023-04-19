// binary search tree
#include <iostream>
using namespace std;

class Node{
    public:
        int data;
        Node *left, *right;
};

class BST {
    public:
        Node *root;
        BST() {
            root = NULL;
        }
        Node *insert(Node *root, int value);
        int search(int searchKey);
}

Node* BST :: insert(Node *root, int value) {
    Node *newNode = new Node;
    newNode->data = value;
    newNode->left = NULL;
    newNode->right = NULL;
    
    if (root == NULL) {
        root = newNode;
    }

    // recursively call function, passing the current node (left or right depending on value) as the new root
    else if (value >= root->data) {
        root->right = insert(root->right, value);
    })
    else {
        root->left = insert(root->left, value);
    }
    return root;
}

// begin with root, and search either left or right of the temp node based on if value > or < current value
int BST :: search(int searchKey) {
    Node *temp = root;
    while (temp != NULL) {
        if (temp->data == searchKey) {
            return searchKey;
        }
        else if (temp->data > searchKey) {
            temp = temp->left;
        }
        else {
            temp = temp->right;
        }
    }
    return -1       // value not found
}

int main() {
    BST tree;
    string ch = "yes";
    int num, searchKey;
    cout<<"Enter the key number:\n";
    cin>>num;

    tree.root = tree.insert(tree.root, num);
    do {
        cout<<"Do you want to create another junction?\n";
        cin>>ch;
        
        if (ch.compare("yes") == 0) {
            cout<<"Enter the key number:\n";
            cin>>num;
            tree.root = tree.insert(tree.root, num);
        }
        else {
            break;
        }
    } while(true);

    cout<<"\nEnter the key to be searched: ";
    cin>>searchKey;
    int flag = tree.search(searchKey);

    if (flag == searchKey) {
        cout<<"\n"<<searchKey<<" found";
    }
    else {
        cout<<"\n"<<searchKey<<" not found";
    }
    return 0;
}