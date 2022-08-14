void quickSort(int l , int h ){
    int x = 0 ; 
    if (l < h) {
        x = partition(l, h);
        quickSort(l,x);
        quickSort(x+1 , h);
       
        
        
    }
}

int partition(int l , int h ) {
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
    return j
}