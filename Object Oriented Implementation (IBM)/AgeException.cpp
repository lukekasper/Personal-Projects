// User defined exception
#include<iostream>
using namespace std;

// inherits funcitonality of built in exception class
class InvalidAgeException: public exception
 {
    string message;
    public:
        //constructor for exception class
        InvalidAgeException(string message) {
            this->message=message;
        }

        // specifies what to return when error is thrown
        string what() {
            return message;
        }
 };

 int main() {
    int age;
    cout<<"Enter Age: "<<endl;
    cin>>age;
    try {
        if (age>5) {
            throw InvalidAgeException("Under Age");
        }
        else if (age>65) {
            throw InvalidAgeException("Over Age");
        }
        else {
            cout<<"Eligible";
        }
    }
    catch(InvalidAgeException e) {
        cerr<<e.what();
    }
 }