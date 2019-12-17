## Use def keyword to declare a function.
## The following is the syntax to declare a function:
# def <function_name>(<arguments>):
## To provide unknown number arguments, use *. For example:
# def add_num(*args):

def isFloat(string1):
    try:
        float(string1)
        return True
    except ValueError:
        return False

num= input("Enter a string (can be numeric or alphabetic): ")
print("The string you entered is a float: ", isFloat(num))