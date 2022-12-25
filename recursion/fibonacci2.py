

def fib(n) :


    num1 = 0 
    num2 = 1
    print( f"{num1} {num2}" ,end = " ")

    for i in range(10) :
        ans = num1 + num2
        print(ans , end =  " ") 
        num1 , num2 = num2 , ans




    return


if __name__ == "__main__" : 
    fib(10)