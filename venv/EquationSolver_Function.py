## This program will solve the linear equations in one variable of the form x + a = b.

def solve_eq(string1):
    x,operator,num1,equal,num2= string1.split()
    num1= int(num1)
    num2 = int(num2)
    if operator=='+':
        print("x =",(num2-num1))
    elif operator=='-':
        print("x =",(num2+num1))
    elif operator=='*':
        print("x =",(num2/num1))
    elif operator=='/':
        print("x =",(num2*num1))

string1= input("Enter equation in the following format: x + 4 = 9 \nNow enter the equation: ")
solve_eq(string1)
