import math 
import heapq as hq
def mergeSortedArrays(arr1, arr2):
    res = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):

        if i >= len(arr1):
            res.append(arr2[j])
            j += 1

        elif j >= len(arr2):
            res.append(arr1[i])
            i += 1

        elif arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1

        else:
            res.append(arr2[j])
            j += 1

        # print(res)

    # print(i, j)
    # while i < len(arr1):
    #     res.append(arr1[i])
    #     i += 1

    # while j < len(arr2):
    #     res.append(arr2[j])
    #     j += 1

    return res


def mergeSortedArrays2(arr1, arr2):
    res = []

    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1

        else:
            res.append(arr2[j])
            j += 1

    while i < len(arr1):
        res.append(arr1[i])
        i += 1

    while j < len(arr2):
        res.append(arr2[j])
        j += 1

    return res


def merge(arr, low, mid, high):
    i = 0
    j = mid + 1

    res = []
    while i <= mid and j <= high:

        if arr[i] < arr[j]:

            res.append(arr[i])
            i += 1
        else:

            res.append(arr[j])
            j += 1

    while i <= mid:
        res.append(arr[i])
        i += 1

    while j <= high:
        res.append(arr[j])
        j += 1

    return res


# using heap 

class Node() :
    def __init__(self , data : int , i : int= None , j : int=  None) -> None:
        self.data = data
        self.i = i 
        self.j = j
        
class MinHeap() :
    def __init__(self,arr : list) -> None:
        self.arr = arr
        self.buildHeap()
        
    def buildHeap(self) -> None : 
        i = (len(self.arr) -2 ) // 2
        while i >= 0:
            # run 
            self.minHeapify(i)
            
            i-=1
            
    def getLeft(self , i : int):
        if (2 * i + 1) < len(self.arr) :
            return 2 * i +1
        return math.inf
    
    def getRight(self , i : int) :
        if (2 * i + 2) < len(self.arr) :
            return 2 * i + 2
        return math.inf
    
    def minHeapify(self , i : int = 0 ) : 
        
        while (
            (self.getLeft(i) or self.getRight(i)) 
            and (self.arr[i] > min(self.arr[self.getLeft(i)] , self.arr[self.getRight(i)]))
        ):
            rep = None
            if self.arr[self.getLeft(i)] > self.arr[self.getRight(i)] : 
                rep = self.getRight(i)
            else :
                rep = self.getLeft(i)
                
            
            
            self.arr[rep] , self.arr[i] = self.arr[i] , self.arr[rep]
            i += rep

    def extractMin(self) -> int:
        
        self.arr[0], self.arr[len(self.arr) - 1] = self.arr[len(self.arr) - 1] , self.arr[0]
        x = self.arr.pop()
        self.minHeapify(0)
        
        return x
        
        
            
            
            
            
            
        

                
        
def mergeKSortedArrays(arr : list) : 


    hp = [li[0] for li in arr ]
    pl = [0 for li in arr]
    
    res = []
    hq.heapify(hp)
    
    while len(hp) : 
        x = hq.heappop(hp)
        res.append(x)

        for p in range(len(pl)) :
            if  len(arr[p]) > pl[p] and x == arr[p][pl[p]] :
                pl[p] += 1 
                if pl[p] < len(arr[p]) : 
                    hq.heappush(hp , arr[p][pl[p]])
                
        
        
    return res
    
    




if __name__ == "__main__":
    # arr1 = [5, 6, 7, 30]
    # arr2 = [10, 15, 20]
    # print(mergeSortedArrays2(arr1, arr2))

    # arr = [10, 15, 20, 11, 13]
    # print(merge(arr, 0, 2, len(arr) - 1))

    # arr = [5, 8, 12, 14, 7]

    # print(merge(arr, 0, 3, len(arr) - 1))
    
    arr= [
        [10,20,30],
        [5 , 15],
        [1 , 9 ,11 ,18]
    ]

    print(mergeKSortedArrays(arr))
    