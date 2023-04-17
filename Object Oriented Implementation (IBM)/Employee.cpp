// illustrate static variables and functions
#include <string> // include string datatype
using namespace std;

class Employee {
    private:
        int empId;
        string name;
        static string compName;

    public:
        static string getCompName() {
            return compName;
        }
};

string Employee::compName="IBM";