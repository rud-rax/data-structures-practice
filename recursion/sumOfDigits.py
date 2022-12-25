
N = 984

def fun(n) : 
    if n == 0 : return 0
    return (n%10) + fun(n//10)

if __name__ == "__main__" :
    print(fun(N))