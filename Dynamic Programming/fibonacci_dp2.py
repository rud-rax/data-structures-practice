
global arr 
arr = [None] * 100

# Solved using Memoization
def fib(n : int) :
    if arr[n] :
        return arr[n]

    if n == 0 or n == 1 :
        arr[n] = n

    else : 
        arr[n] = fib(n-1) + fib(n-2)

    return arr[n]    

if __name__ == "__main__" :
    fib(10)
    print(arr)
