#include<iostream>

using namespace std;

int main() {

    int arr_len {};
    cout << "ENTER THE LENGTH OF ARRAY -> " ;
    cin >> arr_len;
    int arr[arr_len] {};
    for(int i = 0; i < arr_len;i++){
        cout << "ENTER THE ELEMENT AT " << i << " -> ";
        cin >> arr[i]; 
    } 
    cout << "ARRAY = " ;
    for(int i =0 ; i < arr_len ; i++){
        cout << arr[i] << " " ;
    }

    return 0 ;
}