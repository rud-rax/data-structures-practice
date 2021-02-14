#include<iostream>

using namespace std;


int main(){
    int arr[] { 1 , 2 , 3 , 4 , 5 };

    cout << "ARRAY SIZE = " << sizeof(arr) << endl ;
    cout << "SIZE OF EACH ELEMENT = " << sizeof(arr[0]) << endl ;
    for (int i = 0 ; i < (sizeof(arr) / sizeof(arr[0])); i++) {
        cout << "VALUE = " <<  arr[i]  << " ADDRESS = "  << &arr[i] << endl;
    }
    return 0;

}
