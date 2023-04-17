// Illustrates exception handling
#include<iostream>
using namespace std;

class Printer {
    private:
        string name;
        int paperCount;
    public:
        Printer(string name, int paperCount) {
            this->name=name;
            this->paperCount=paperCount;
        }

        void displayPrint(string printContent) {
            // perform normal print logic
            if (paperCount>0) {
                cout<<printContent<<endl;
                paperCount--;
            }
            // if no pages are left, throw an error message
            else {
                throw "WARNING! REFILL PAPER";
            }
        }
};

int main() {
    // suspect code to try
    try {
        Printer obj("HP",2);
        obj.displayPrint("Hello");
        obj.displayPrint("Hello again");
        obj.displayPrint("Hello one more time");
    }

    // catch thrown error messages
    catch(const char* errorMessage) {
        cerr<<errorMessage<<endl;
    }
}