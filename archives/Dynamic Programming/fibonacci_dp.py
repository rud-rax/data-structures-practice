
# Solved using Tabulation
def fib(arr , n ) :

    if n == 1 :
        return [0,1]
    if n == 0 :
        return [0]

    for i in range(n-1) : 
        arr.append(arr[-1] + arr[-2])

    return arr
if __name__ == "__main__" :
    arr = [0,1]
    print(fib(arr , 10))
