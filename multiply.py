

def multiply_list(input):
    """
    Take in as input a list
    The function multiply_list() will multiply all of the numbers in the list.
    If any item in the list is invalid return False.
    
    """
    result = 1
    #if there is no numbers in list return False
    if not input:
        return False
    #if the list contains strings or 0 return False
    else:    
        for x in input:
            if type(x) == str or x == 0:
                return False       
            else:
                result = result*x
        return result