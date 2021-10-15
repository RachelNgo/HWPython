

def multiply_list(input):
    """
    
    """
    #if there is no numbers in list return False
    if not input:
        return False
        
    
    
    #if  in list contains string return False
    for x in input:
        if type(x) == str:
            return False
   
    else:
        # start the product by 1 because 0 will return 0
         result = 1
         for x in input:
            if x == 0:
                return False
            else:
                result = result * x

    return result