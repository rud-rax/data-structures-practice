def solve(n) :
    c = 0 
    while n > 0 : 

        for i in range(1,100) :
            if n < (i**2) : 
                n -= (i - 1 )**2
                c+=1
                break

    return c



print(solve(40))