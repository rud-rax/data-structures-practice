
import math

def linear_search(ll,value):
    for i in range(len(ll)):
        if ll[i] == value :
            return i
    return None
    
def bidirectional_linear_search(ll,value):
    for i in range(len(ll)//2):
        if ll[i] == value :
            return i
        if ll[len(ll) -1  - i ] == value:
            return len(ll) - i -1
    return None

def binary_search_recursive(ll,value,l,r):
      
    if r < l : return None

    mid = (r + l) // 2 

    if ll[mid] == value : return mid

    elif ll[mid] < value : return binary_search_recursive(ll,value,mid + 1,r)
    
    elif ll[mid] > value : return binary_search_recursive(ll,value,l,mid - 1)

def binary_search_iterative(ll,value):
    l = 0
    r = len(ll) - 1
    
    while l <= r :
        mid = (l + r) // 2

        if ll[mid] == value : return mid

        elif ll[mid] < value :
            l = mid + 1

        elif ll[mid] > value :
            r = mid - 1
    else : return None

def jump_search(ll,value,n = math.sqrt(len(ll))):
    while ll[n] < value :
        n += math.sqrt(len(ll))
    return linear_search(ll[n - math.sqrt(len(ll)):n+1],value)


if __name__ == "__main__":
    l = [7,1,4,6,2,8,0]
    l1 = [7,1,4,6,2,8]
    sl = [3,5,6,8,9,10]
    sl1 =[3,5,6,7,8,9,10]

    print("LINEAR SEARCH = " , p1 := linear_search(l,8))
    print("BIDIRECTIONAL LINEAR SEARCH = " ,p :=bidirectional_linear_search(l,8))
    print("RECURSIVE BINARY SEARCH = " , bin_s := binary_search_recursive(sl,8,0,len(sl) - 1 ))
    print("ITERATIVE BINARY SEARCH = " , bin_s1 := binary_search_iterative(sl1 , 5))
    print("JUMP SEARCH = ", jp := jump_search(sl,7))


