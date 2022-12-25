


def fib(n) :
    if n == 1 :
        return 1 
    if n == 0 :
        return 0

    return fib(n-1) + fib(n-2)

if __name__ == "__main__" :
    
    for i in range(10) :
        print(fib(i) , end = " ")