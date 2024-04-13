
import random


def insertion_sort(array):
    for i in range(1,len(array)):
        for j in range(i):
            if array[j] > array[i]:
                array[j],array[i] = array[i],array[j]
    return array

def selection_sort(array): 
    for i in range(len(array)):
        for j in range(len(array)-1,0,-1):
            if array[i] > array[j]:
                array[i],array[j] = array[j],array[i]
    return array

def bubble_sort(array):
    for i in range(1,len(array)):
        for j in range(len(array)-i):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array

def selection_sort2(array):
    for i in range(len(array)):
        k = i
        for j in range(i+1,len(array)):
            if array[j] < array[k]:
                k = j
            if (k != i):
                array[i],array[k] = array[k],array[i]
    return array
        
def insertion_sort2(array):
    i = 0
    while i < len(array):
        j =0
        while j < i :
            if array[i]<array[j]:
                array[i],array[j] = array[j],array[i]
            j+=1
        i+=1
    return array

if __name__ == "__main__":
    l = [2,5,9,1,8,7]
    lr = [random.randint(1,30) for _ in range(10)]
    print(lr)
    l3 = [15, 18, 16, 4, 5, 9, 28, 11, 19, 10]
    print("INSERTION SORT LIST : ",insertion_sort2(l))
    print("INSERTION SORT LIST : ",insertion_sort2(l3))
    print("SELECTION SORT LIST : ",selection_sort2(l))
    print("SELECTION SORT LIST : ",selection_sort2(l3))
    print("BUBBLE SORT LIST : ",bubble_sort(l))
    print("BUBBLE SORT LIST : ",bubble_sort(l3))