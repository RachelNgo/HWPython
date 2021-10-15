def calculator(number1, number2, operator):
    """
    The calculator function take three parameters in this order. 
    Return the result of the operation but if it was invalid return False.
    """
    if(operator == "+"):
        return number1 + number2
    elif(operator == "-"):
        return number1 - number2
    elif(operator == "*"):
        return number1 * number2
    elif(operator == "/"):
        return number1 / number2
    elif(operator == "//"):
        return number1 // number2
    elif(operator == "**"):
        return number1 ** number2
    else:
        return False
def parse_input():
    """
    This function will take input from the user and call the calculator function.
    """
    userInput = input("Enter equation: ")
    num1, operations, num2 = userInput.split(" ")
    num1 = float(num1)
    num2 = float(num2)
    print(calculator(num1, num2, operations))

