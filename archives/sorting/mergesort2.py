

def merge(arr , low , mid , high) :

    mm = mid +1
    res = []
    k = 0
    while low < mid and mm <= high :
        if arr[low] < arr[mm] :
            # res.append(arr[low])
            k += 1
            low +=1 
        else :
            # res.append(arr[mm])
            arr.insert(arr[mm] , k)
            arr.remove(arr[mm + 1])
            low +=1
            mid += 1
            k +=1
            mm +=1

    while low < mid :
        res.append(arr[low])
        low +=1

    while mm <= high :
        res.append(arr[mm])
        mm +=1

    i = 0
    while res[i] < arr[mid] :
        i+=1

    res.insert(i , arr[mid])
    return res

    
def merge2(arr , low , mid , high) :

    mm = mid +1
    res = []
    while low < mid and mm <= high :
        if arr[low] < arr[mm] :
            res.append(arr[low])
            low +=1
        else :
            arr.append(arr[mm])
            mm +=1

    while low < mid :
        res.append(arr[low])
        low +=1
    
    while mm <= high :
        res.append(arr[mm])
        mm+=1

    for i in range(len(res)) :
        if not res[i] < arr[mid] :
            break
        
    res.insert(i , arr[mid])

    arr = res
    print(arr)

    
def merge3(arr , low , mid , high) :
    mm = mid + 1

    while low <= mid and mm <= high : 
        if arr[mm] < arr[low] :
            arr.insert(low , arr[mm])
            arr.pop(mm +1)
            low +=1
            mid +=1
            mm +=1
        else :
            low +=1

    

    print(arr)

def mergeSort(arr , low , high) :
    if low < high : 
        m = (low + high) // 2
        mergeSort(arr , low , m)
        mergeSort(arr , m + 1 , high)
        merge3(arr , low , m ,  high)

if __name__ == "__main__" :
    # arr = [4 , 6 , 19 , 11 , 5 , 7 , 13 , 22]
    # arr = [1,3,11 , 30 , 35 , 4 , 5 , 7 , 13 , 22]
    # arr=[3,1]

    # merge3(arr , 0, 0 , len(arr) - 1)


    arr = [3,5,2,1,7,4,6]
    mergeSort(arr , 0 , len(arr) - 1)
    # print(arr)