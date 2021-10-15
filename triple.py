def tripler(myFunction):
    """
    This decorator takes in a function. 
    The function is called three times and return it.
    """
    def wrapper():
        myFunction()
        myFunction()
        myFunction()
    return wrapper
@tripler
def callTripler():
    print("Python is Cool")
callTripler()

