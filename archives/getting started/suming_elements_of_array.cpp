#include<iostream>
#include<vector>
using namespace std ;

int main (){
    
    // USING ARRAYS 
    int arr[5] { 10 , 20 , 30 , 40 , 50 };
    int arr_len = sizeof(arr) / sizeof(arr[0]);
    int arr_sum {};
    cout << "ARRAY LENGTH = " << arr_len << endl;
    for (int i = 0 ; i < arr_len ; i++){
        cout << "VALUE = " << arr[i] << endl;
        arr_sum += arr[i];
    }
    cout << "SUM OF ARRAY = "<< arr_sum << endl;


    // USING VECTORS
    vector <int> vec {100 , 200 , 300 ,  400 , 500 };
    int vec_sum {};
    cout << "VECTOR LENGTH  = " << vec.size() << endl;
    for( int i = 0 ; i < vec.size() ; i++)  {
        cout << "VALUE = " << vec[i] << endl;
        vec_sum += vec[i];

    }
    cout << "SUM OF VECTOR = " << vec_sum << endl;
    return 0;
}