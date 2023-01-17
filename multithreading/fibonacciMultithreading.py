
import concurrent.futures
import time
import threading

global FUNCTION_DELAY
FUNCTION_DELAY = 0.1



def fibonacciMultithreading(n) :
    time.sleep(FUNCTION_DELAY)

    if n == 0 or n == 1 :
        return n
    
    with concurrent.futures.ThreadPoolExecutor() as executor :
        threads = [executor.submit(fibonacciMultithreading , n-i) for i in range(1,3) ]

        x = 0 
        for thread in concurrent.futures.as_completed(threads) :
            x+= thread.result()
    
    
    return x

def fibonacciStatic(n) :
    time.sleep(FUNCTION_DELAY)

    if n == 0 or n == 1 :
        return n

    return fibonacciStatic(n-1) + fibonacciStatic(n-2)

def fibonacciDynamicProgramming(n) :
    arr = []

    time.sleep(FUNCTION_DELAY)
    arr.append(0)

    time.sleep(FUNCTION_DELAY)
    arr.append(1)

    for i in range(2,n+1) :
        time.sleep(FUNCTION_DELAY)
        arr.append(arr[-1] + arr[-2])
    
    return arr[-1]


def runFunction(function,*params):

    start = time.perf_counter()
    print(function(params[0]))
    stop = time.perf_counter()

    timeTaken = round(stop - start , 2)
    print(f"Time taken for execution of {function.__name__} is {timeTaken} seconds.")
    return timeTaken


def chatGPTcode(n) :


    def fibonacci(n):
        time.sleep(FUNCTION_DELAY)
        if n < 0:
            return "Invalid input"
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    # Create a new thread to compute the Fibonacci number
    thread = threading.Thread(target=fibonacci, args=(n,))

    # Start the thread
    thread.start()

    # Wait for the thread to complete
    thread.join()



if __name__ == "__main__" :

 
    n = 8

    # timeTakenStatic = runFunction(fibonacciStatic,n)
    timeTakenMultithreading = runFunction(fibonacciMultithreading,n)
    timeTakenDynamicProgramming = runFunction(fibonacciDynamicProgramming,n)



    timeTakenChatGPT = runFunction(chatGPTcode , n)




