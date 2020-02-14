# We use finally keyword when we want a certain block of code to execute no matter whether an exception is raised or not.
# We use else when we want a certain block of code to execute only when no exceptions are raised.
num1, num2 = map(int, input("Enter two numbers: ").split())

try:
    div = num1/num2
except ZeroDivisionError:
    print("Sorry you cannot divide by zero.")
else:
    print("{} / {} = {}".format(num1,num2,div))
finally:
    print("Program ends here.")