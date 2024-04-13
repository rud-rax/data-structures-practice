
N = 10

def solve(n) :
    
    if n == 0 :
        return 

    solve(n-1)
    print(n , end = " ")


if __name__ == "__main__" :
    solve(N)