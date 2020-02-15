# Lambda function are one liner functions in Python. We can use them when we need a function to solve a specific problem but we don't want to make our function look messy by defining an entire new function for it. Given below is an example of how you can define a lambda function.
# lambda arg1, arg2 : arg1 + arg2

"""
num1, num2 = map(int, input("Enter two numbers: ").split())

sum = lambda num1, num2: num1 + num2

print(sum(num1,num2))

"""

can_vote = lambda age: True if age>=18 else False
age = int(input("Enter the age: "))
print("Can the person vote: {}".format(can_vote(age)))