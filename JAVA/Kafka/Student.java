// Java program to implement a
// student class

// Creating a student class
public class Student {

    // Data members of the class
    int id;
    String firstName;
    String lastName;

    // Constructor of the student
    // Class
    public Student()
    {
    }

    // Parameterized constructor of
    // the student class
    public Student(int id, String firstName,
                   String lastName)
    {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
    }

    // Implementing the getters
    // and setters
    public int getId()
    {
        return id;
    }

    public void setId(int id)
    {
        this.id = id;
    }

    public String getFirstName()
    {
        return firstName;
    }

    public void setFirstName(String firstName)
    {
        this.firstName = firstName;
    }

    public String getLastName()
    {
        return lastName;
    }

    public void setLastName(String lastName)
    {
        this.lastName = lastName;
    }

    @Override
    public String toString()
    {
        return "Student{"
            + "id = " + id
            + ", firstName = '" + firstName + "'"
            + ", lastName = '" + lastName + "'"
            + "}";
    }
}
