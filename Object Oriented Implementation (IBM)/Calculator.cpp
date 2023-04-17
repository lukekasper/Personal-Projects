// Template Class
template <class T1, class T2> class Calculator {
    private:
        // attributes
        T1 number1;
        T2 number2;
    public:
        //constructor
        Calculator(T1 number1, T2 number2) {
            this->number1=number1;
            this->number2=number2;
        }
        void calculateSum();
        void calculateDifference();
};

// use template decleration syntax to define method outside of the class scope
template <class T2, class T2> void Calculator<T2, T2>::calculateSum() {
    cout<<"Sum = "<<number1+number2<<endl;
}

template <class T2, class T2> void Calculator<T2, T2>::calculateDifference() {
    cout<<"Difference = "<<number1-number2<<endl;
}

int main() {
    // specify data type when creating object
    Calculator<int,double> c1(2,10.5);
    c1.calculateSum();
    c1.calculateDifference();
}