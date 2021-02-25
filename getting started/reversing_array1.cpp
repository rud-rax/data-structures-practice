#include<iostream>

using namespace std;

int main() {
    
    int arr_len {};
    cout << "ENTER THE LENGTH OF THE ARRAY -> " ;
    cin >> arr_len ;
    int arr [arr_len] {};

    for(int i = 0; i < arr_len ; i++){
        cout << "ENTER THE ELEMENT AT " << i << " -> " ;
        cin >> arr[i] ;
    }

    cout << "ARRAY = ";
    for (int i = 0 ; i < arr_len ; i++){
        cout << arr[i] << " " ;
    }

    int temp {};
    
    for(int i = 0 ; i < arr_len / 2  ; i++){
        temp = arr[i];
        arr [i] = arr[arr_len - i - 1 ];
        arr[arr_len - i - 1 ] = temp ;
    }

    cout << endl << "REVERSED ARRAY = " ;
    for (int i = 0 ; i < arr_len ; i++){
        cout << arr[i] << " " ;
    }

    return 0;
}