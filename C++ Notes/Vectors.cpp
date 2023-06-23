#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    // sort: sorts vector in ascending order
    vector<int> numbers = {5, 2, 8, 1, 9};
    sort(numbers.begin(), numbers.end());

    // find: searches for a specific value in a vector and returns an iterator pointing to the first occurrence
    int searchValue = 8;
    auto it = find(numbers.begin(), numbers.end(), searchValue);
    if (it != numbers.end()) {
        cout << "Value " << searchValue << " found at position " << distance(numbers.begin(), it) << endl;
    } else {
        cout << "Value " << searchValue << " not found." << endl;
    }

    // count: counts the number of occurrences of a specific value in a vector
    int countValue = 2;
    int count = count(numbers.begin(), numbers.end(), countValue);

    // reverse vector order
    reverse(numbers.begin(), numbers.end());
    cout << "Reversed numbers: ";
    for (const auto& num : numbers) {
        cout << num << " ";
    }
    cout << endl;

    // accumulate: sums the vector
    int sum = accumulate(numbers.begin(), numbers.end(), 0);

    // max (or min) element
    auto it = max_element(numbers.begin(), numbers.end());

    // binary_search: checks if value exists in a sorted vector using binary search
    int searchValue = 5;
    bool found = binary_search(numbers.begin(), numbers.end(), searchValue);

    // transform: applies a specific operation to each element and stores the result in a new vector
    vector<int> squaredNumbers;
    transform(numbers.begin(), numbers.end(), back_inserter(squaredNumbers), [](int num) {
        return num * num;
    });

    // unique: removes conecutive duplicate elements from a vector
    numbers.erase(unique(numbers.begin(), numbers.end()), numbers.end());

    return 0;
}