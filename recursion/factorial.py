

def fact(n) :
    if n == 0 :
        return 1


    return n * fact(n-1)

if __name__ == "__main__" :
    
    for i in range(10) :
        print(fact(i) , end = " ")