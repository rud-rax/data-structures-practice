from math import ceil
import math

class Heap:
    def __init__(self, arr: list = []) -> None:

        self.arr = arr
        self.buildHeap()
        
    def buildHeap(self) :
        i = ceil(len(self.arr) - 2) // 2
        while i >= 0 :
            if self.getLeft(i) or self.getRight(i) :
                
                self.minHeapify(i)
            i-=1

    def getLeft(self, i):
        if (2 * i + 1) < len(self.arr):
            return self.arr[2 * i + 1]
        return math.inf

    def getRight(self, i):
        if (2 * i + 2) < len(self.arr):
            return self.arr[2 * i + 2]
        return math.inf

    def getParent(self, i):
        if i:
            return self.arr[(i - 1) // 2]
        return None

    def insert(self, n):
        i = len(self.arr)
        self.arr.append(n)

        while self.getParent(i) and self.getParent(i) > self.arr[i]:
            self.arr[i], self.arr[(i - 1) // 2] = self.arr[(i - 1) // 2], self.arr[i]
            i = (i - 1) // 2

    def minHeapify(self , i :int = 0 ):



        while (
            (self.getLeft(i) or self.getRight(i))
            and (self.arr[i] > min(self.getLeft(i), self.getRight(i)))
        ):
            rep = None
            if self.getLeft(i) > self.getRight(i):
                rep = 2 * i + 2
            else:
                rep = 2 * i + 1

            self.arr[i], self.arr[rep] = self.arr[rep], self.arr[i]
            i = rep
        
        # arr = self.arr
        # n = len(arr)

        # li = 2 * i +1
        # ri = 2 * i +2
        
    def extractMin(self) : 
        self.arr[0]  ,self.arr[len(self.arr) - 1] =  self.arr[len(self.arr) - 1] , self.arr[0]
        self.arr.pop()
        self.minHeapify()
        
        # self.deleteKey(0)
        
        
    def decreaseKey(self , i : int , x : int) :
        
        self.arr[i] = x
        
        while self.getParent(i) and self.getParent(i) > self.arr[i]:
            self.arr[i] , self.arr[(i - 1) // 2 ] = self.arr[(i - 1) // 2 ] , self.arr[i] 
            i = (i - 1) // 2

    def deleteKey(self,i : int) :
        self.arr[i] , self.arr[len(self.arr) - 1] = self.arr[len(self.arr) - 1] , self.arr[i]
        self.arr.pop()
        self.minHeapify(i)

if __name__ == "__main__":
    hp = Heap([60, 20, 15, 40, 50, 100, 25, 45])
    
    # print(hp.arr)
    # i = 1
    # print(hp.getLeft(i))
    # print(hp.getRight(i))
    # print(hp.getParent(i))

    # print(hp.arr)
    # hp.insert(12)
    # print(hp.arr)
    # hp.insert(9)
    # print(hp.arr)
    
    # hp = Heap([2, 5, 4, 3])
    # print(hp.arr)
    # hp.minHeapify()
    # print(hp.arr)
    
    # hp = Heap([10,20,30,40,50,35 , 38 , 45])
    # print(hp.arr)
    # hp.extractMin()
    # print(hp.arr)
    
    # hp = Heap([20 ,80, 200 , 90 , 100 , 250 , 500 , 120])
    # hp.decreaseKey(3,10)
    # print(hp.arr)
    
    # hp = Heap([10,20,30,40,50,35 , 38 , 45])
    # print(hp.arr)
    # hp.deleteKey(i = 3)
    # print(hp.arr)
    # hp.deleteKey(i = 0)
    # print(hp.arr)
    
    # hp = Heap([10 ,5, 2, 20 , 1, 40 , 15 , 5 , 11])
    # print(hp.arr)
