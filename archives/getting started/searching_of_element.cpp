#include<iostream>

using namespace std;

int main(){

    int arr[10] = {5,2,4,6,8,1,9};
    int search_element {};
    cout << "ENTER AN ELEMENT TO BE SEARCHED IN THE ARRAY -> " ;
    cin >> search_element ;
    bool found = false ;
    for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++){
        if (arr[i] == search_element){
            cout << "ELEMENT FOUND AT INDEX = " << i << endl;
            found = true ;
            break ;
        }
    }

    if (!found) 
        cout << "ELEMENT NOT FOUND " << endl;

    return 0;
}