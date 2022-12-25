

import logging
import time

def logActivity(original_function) :
    logging.basicConfig(filename= f"decorators/{original_function.__name__}.log" , level= logging.INFO)

    def wrapper_function(*args , **kwargs) :
        logging.info(f"Ran with args = {args} and kwargs = {kwargs} at time {time.time()}")
        return original_function(*args , **kwargs)

    return wrapper_function

@logActivity
def display(name , age) :
    print(f"Hi, I am {name} and my age is {age}")

# display("Rud" , 21)
# display("Jerry" , 4)
display("Tom" , 9)