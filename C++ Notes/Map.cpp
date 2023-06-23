// map is similar to a dictionary in other languages
#include <iostream>
#include <map>

using namespace std;

int main() {
    map<string, int> ages = {
        {"Alice", 25},
        {"Bob", 30},
        {"Charlie", 35}
    };

    // find: returns an iterator pointing to the element if found
    // an iterator in this case contains a key-value pair corresponding to the map, which can be accessed using .first or .second
    auto it = find(ages.begin(), ages.end(), make_pair("Bob", 30));

    if (it != ages.end()) {
        cout << "Bob found. Age: " << it->second << endl;
    } else {
        cout << "Bob not found." << endl;
    }

    // count: counts occurences of a specific key in the map
    map<string, int> wordCount = {
        {"apple", 3},
        {"banana", 2},
        {"cherry", 5},
        {"apple", 1}
    };
    int count = count(wordCount.begin(), wordCount.end(), make_pair("apple", 3));

    // lower_bound: finds iterator pointing to the first element in the map that is not less than a specified key
    map<int, string> students = {
        {1001, "Alice"},
        {2002, "Bob"},
        {3003, "Charlie"}
    };

    int key = 2002;
    auto it = lower_bound(students.begin(), students.end(), make_pair(key, ""));

    if (it != students.end() && it->first == key) {
        cout << "Student found: " << it->second << endl;
    } else {
        cout << "Student not found." << endl;
    }

    // erase: removes element from map based on specified key or range of iterators and returns the number of elements erased
    string key = "apple";
    auto numErased = wordCount.erase(key);

    // emplace: constructs and inserts a new element into the map
    wordCount.emplace("peach", 4);

    // perform operations on the keys and values in a map
    // Loop over the map and print the keys and values
    for (const auto& pair : ages) {
        const string& name = pair.first;
        int age = pair.second;

        cout << "Name: " << name << ", Age: " << age << endl;
    }

    // Perform operations on keys and values
    for (auto& pair : ages) {
        string& name = pair.first;
        int& age = pair.second;

        // Convert the name to uppercase
        for (char& c : name) {
            c = toupper(c);
        }

        // Increment the age by 1
        age++;
    }

    // Print the updated map
    for (const auto& pair : ages) {
        const string& name = pair.first;
        int age = pair.second;

        cout << "Name: " << name << ", Age: " << age << endl;
    }

    return 0;
}
