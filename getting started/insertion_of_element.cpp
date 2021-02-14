#include<iostream>

using namespace std;

int main(){

    int arr[30] =  {5,1,7,9,4};
    int element {} , index {};
    cout << "ENTER ELEMENT TO INSERT AND ITS INDEX --> " ;
    cin >> element >> index;
    int old_element = element;
    int new_element {};
    for (int i = index; i < sizeof(arr) / sizeof(arr[0]); i++) {
        new_element = arr[i];
        arr[i] = old_element;
        old_element = new_element;
    }

    for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++)
        cout << arr[i] << " ";

    return 0 ;
    
}