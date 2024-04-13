#include<iostream>
#include<vector>

using namespace std ;

int main() {

    // USING ARRAYS 
     int arr[] {5,1,9,8,2,4,5,1};
     int element_index{};
     cout << "ENTER THE ELEMENT TO DELETE = " ;
     cin >> element_index;
    for(int i = element_index ; i < (sizeof(arr) / sizeof(arr[0])) - 1 ; i++){
        arr[i] = arr[i+1];
    }    
    cout << "NEW ARRAY = ";
    for(int i = 0 ; i < (sizeof(arr) / sizeof(arr[0])) - 1 ; i++){
        cout << arr[i] << " " ;
    }    

    return 0;


}