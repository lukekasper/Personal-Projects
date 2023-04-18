// stack implementation using array data structure
#define MAX 10
class Stack {
    int top;
    public:
        int arr[MAX];           // array size
        
        // constructor for stack to assign top variable to -1 (empty)
        Stack() {
            top = -1;
        }

        // declare push, pop, and peek member functions for outside definition
        void push(int item);    
        int pop();
        int peek();
};

// push either returns a message if array size is exceeded, or incrememnts the "top" variable and adds item to that index
void Stack::push(int item) {
    if (top >= (MAX - 1)) {
        cout<<"\nStack overflow";
    }
    else {
        arr[++top] = item;
        cout<<"\nElement added"<<item; 
    }
}

// returns error message if array is empty, or decrement top variable and return item
int Stack::pop() {
    if (top < 0) {
        cout<<"\nStack underflow";
        return -1;
    }
    else {
        int item = arr[top--];
        return item;
    }
}

// same thing as pop but returns top item without decrementing
int Stack::peek() {
    if (top < 0) {
        cout<<"\nStack underflow";
        return -1;
    }
    else {
        int item = arr[top];
        return item;
    }
}