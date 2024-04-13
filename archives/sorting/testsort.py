

def partition( arr , l , h ) :
    piv = l 
    i = l
    
    for j in range(i + 1, h) :
        if arr[j] < arr[piv] : 
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
            
    arr[i] , arr[piv] = arr[piv] , arr[i]
    # print(arr)
    return i
        
    
def quickSort(arr , l , h ) :
    if  l < h :
        i = partition(arr , l , h )
        quickSort(arr, l , i)
        quickSort(arr , i+1 , h )  
    
if __name__ == "__main__" :
    
    arr = [3,4,1,5,2]
    arr = [14, 12, 70, 15, 95, 65, 22, 30]
    
    quickSort(arr , 0 , len(arr))
    # i = partition(arr , 0 , len(arr) )
    print(arr)