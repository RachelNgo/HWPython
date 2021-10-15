import time
def calculate_time(test_time):
    """
    A decorator to calculate the time to run a function.
    """
    # get the start and end time in sec
    def wrapper():
        startTime = time.time()
        test_time()
        endTime = time.time()
        print("Total time: ", endTime - startTime)   
    return wrapper   
# decorator function
@calculate_time
def runtime():
    """[ the compiler will execute the fixed time delay]
    """
    time.sleep(2)
runtime()
 

