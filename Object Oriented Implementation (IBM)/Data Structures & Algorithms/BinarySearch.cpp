// binary search algorithm
#include <iostream>
using namespace std;

bool binarySeach(int arr[], int key, int low, int high) {
    int middle = (low + high)/2;
    while (low <= high) {
        if (arr[middle] == key) {
            return true;
        }
        else if (arr[middle] < key) {
            low = middle + 1;
        }
        else {
            high = middle - 1;
        }
        middle = (low + high)/2;
    }
    return false;
}

int main() {
    int i, arr[10], key;
    cout<<"Eneter 10 elements (in ascending order): ";
    for (i=0; i<10; i++) {
        cin>>arr[i];
    }
    cout<<"\nEnter Element to be Searched: ";
    cin>>key;
    bool result = binarySeach(arr, key, 0, 5);
    if (result != false) []
        cout<<"\nElement found";
    else {
        cout<<"\nElement not found";
    }
    return 0;
}