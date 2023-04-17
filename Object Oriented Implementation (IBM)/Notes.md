## Classes and Objects
- A class is the generalized blueprint for which objects are constructed from
  - describes the state (data or attributes) and behavior that an object of this type supports
  - fundamental building block of C++
- An object is an instance of a class
  - syntax: class_name object_name (ie Employee empObj)
  - when object is created, all data members are assigned default values
- Attributes are instance variables or data memebers or class variables
  - used to declare properties of a class (called data members)
  - can be intrinsic type (int, double, ect), or user defined type (a class)
  - syntax of an attribute:
    - private: double salary
- Methods define behavior of an object derived from the class
  - will have a name and return type (void means no return type)
- Access to attributes and members is done with "."
- Scope resolution operator "::" used to declare member functions outside of the class
  - double Employee::calculateGrossPay(int bonus){}
  - signature of method should still be in class (double calculateGrossPay(int bonus);)
- Information hiding is implemented using access Specifiers or visbility modifiers
  - regulate access to classes, fields, and methods
  - specify if a field or method in a class can be accessed from another class or subclass
  - public: accessed anywhere
  - private: only accessed within that class (default)
  - protected: accessed within class and subclasses

## Member Functions
- Instance methods: Accessor (or Getters) and Mutators (or Setters) are public methods that allow the user to manipulate an object's data
- Accessors don't change the state of the object
  - getSalary(): accepts no parameters but returns salary
- Mutators change the object state
  - setSalary(): take parameter as an input to set a data member
- Constructors: a method that is envoked when an object is created to initialize the instance variables to a default value
  - name should be the same as the name of the class
  - must not have any return type (not even a void)
  - 3 types: 
    - default: no arguements, all objects created will have the same default values
    - parametrized: takes an arguement list, different default values for each object
      - when creating an object from that class, pass the default values in as parameters to utilize this constructor 
      - Employee empObj(101, "rex", 25000);
    - copy: initialize an object using another object of the same class
      - shallow (member-wise) copy: C++ copies each member of the class individually using the assignment operator
        - Employee e1 = e;
      - deep copy: copies all fields and makes copies of dynamically allocated memory pointed to by fields
  - a singleton class is one that has a private constructor, can only be initialized by its own member functions
  - if a local variable shadows a field with the same name, use "this" pointer
    - this->empid=empid; (for public parameterized constructor
    - use also if a method needs to pass the current object to another method
    - "this" refers to the current object and stores the address of the current object
  - overloading: 
    - a class can have multiple constructors or methods with the same name but they must vary in:
      - number of parameters
      - type of parameters
      - order of parameters
    - behavior differs based on arguements
    - difference in return type is not a valid overloading scenario
- Destructors: de-allocates memory
  - compiler provides defualt destructor when none are provided
  - cannot take arguements or return values
  - called with "~"


## Static
- static or class variables: properties associated to a class but not a specific object (global to all objects of a class)
- can access static properties through static member functions
- "this" pointer cannot be used for static variables
- static data must be initialized outside of the class using "::"

## Inheritance
- common properties and methods across multiple classes can be collected in a parent class
- ability to reuse methods and properties of parent class
- parent class constructor is envoked before specific contructors/methods of the child class
  - destructors are called in the opposite order
- if private, properties of parent class can only be accessed in child class through getters/setters
- Types of inheritance: 
  - single: derived class is inherited from a single parent class
  - multiple: inherits attributes from 2+ base classes
  - hierarchical: derive more than one class from a parent class
  - multilevel: parent class of one derived class is itself derived from another parent class
  - hybrid: combination of inheritance types
- inheritence is invoked through "class <parent> : <access modifier> <child>
  
## Polymorphism
- ability for a method to do different things based on the object it is acting on
- when two methods have the same name and invocation in parent and child class, use "virtual" key word in base class method 
- method overriding is using a pointer to hold the address for a specific object to ensure correct class method is invoked
  - a pointer is invoked through: "<class_name> * <pointer_name> = &<object_name>"
  - pointers that refer to the base class can only rerfer to members that the subclass objects inherit from the base class
- a virtual function is declared in a baseclass and then overriden (or redefined) in a derived class
- when you refer to a sub class object using a pointer, you can:
  - call a virtual function for that object
  - execute the version of the function of that sub class
- two types of polymorphism:
  - static binding (or compile time):
    - performed at compile time
    - acheived through method overloading
  - dynamic binding (or runtime):
    - acheived through method overriding
- abstract base class: comprised of at least one pure virtual function
  - a pure virtual function (or member) is set =0
  - if defining a pure virtual member to the base class, you must add the member to ANY derived class
