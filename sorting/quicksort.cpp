#include<iostream>
#include<vector>
using namespace std ;

int partition( vector<int> arr,int l , int h ) {
    int i = l, j = h ;
    
    while (i < j){
        while (arr[l] <= arr[i] && i < j) {
            i+=1 ; 
        }
        while (arr[l] > arr[j]){
            j-=1 ; 
        }
        if (i < j ){
            arr[i] , arr[j] = arr[j],arr[i] ;
            
        }
    }
    arr[l],arr[j] = arr[j],arr[l] ;
    return j;
}

void quickSort(vector<int> arr,int l , int h ){
    int x = 0 ; 
    if (l < h) {
        x = partition(arr , l, h);
        quickSort(arr,l,x);
        quickSort(arr, x+1 , h);
       
    }
}

int main() {
    vector<int> arr{4,2,1,5,3} ;

    quickSort(arr , 0 , arr.size()) ;
    return 0 ;

}