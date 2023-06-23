#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    string text = "Hello, world!";

    // search: search for substring and return position of first occurence
    string search = "world";
    auto position = text.find(search);

    // replace
    char search = 'o';
    char replacement = 'x';
    replace(text.begin(), text.end(), search, replacement);

    // substring: extract a substring based on a given position and length
    size_t position = 7;
    size_t length = 5;
    string substring = text.substr(position, length);

    // count: count number of occurences of a char in a string
    char countChar = 'l';
    int count = count(text.begin(), text.end(), countChar);

    // reverse: reverses characters in a string
    reverse(text.begin(), text.end());

    // toupper (or tolower): convert all chars to upper or lower
    transform(text.begin(), text.end(), text.begin(), ::toupper);

    // isdigit: checks if all chars in a string are digits
    bool allDigits = all_of(text.begin(), text.end(), ::isdigit);

    // find_first_of: find position of first occurence of any char from a set of chars in a string
    string charsToFind = "o!$";
    auto position = text.find_first_of(charsToFind);
    if (position != string::npos) {
        cout << "First occurrence found at position " << position << endl;
    } else {
        cout << "No occurrences found." << endl;
    }

    // replace_if: replace chars in a string based on a given predicate
    // example replaces all uppercase characters with '*'
    replace_if(text.begin(), text.end(), [](char c) {
        return isupper(c);
    }, '*');