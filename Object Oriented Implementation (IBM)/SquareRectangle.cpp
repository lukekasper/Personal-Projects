// Illustrates concepts of operator overloading and friend function
#include<iostream>
using namespace std;
class Square; // forward decleration (not necessary)
class Rectangle {
    // attributes
    private:
        int length;
        int breadth;
    
    // constructor and methods
    public:
        Rectangle(int length, int breadth) {
            this->length=length;
            this->breadth=breadth;
        }
        
        // overload '>' operator using friend function to include Rectangle class
        friend void operator > (Rectangle rq, Square s2);   // binary operator
};

class Square {
    //attributes
    private:
        int length;
    
    // constructor and methods
    public:
        Square(int length) {
            this->length=length;
        }
        
        // overload '>' operator to make Square class available
        friend void operator > (Rectangle rq, Square s2);
};

// non-member function definition for overloaded operator
void operator >(Rectangle r1, Square s2) {
    r1.length>s2.length?cout<<"Length of Rect is more":cout<<"Length of Sq is more";
}

int main() {
    Rectangle obj1(1, 2);
    Square obj2(4);
    obj1>obj2;
}