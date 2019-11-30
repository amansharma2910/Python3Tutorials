# We use variable_name = input() syntax to take the input in Python. Remember that all the input in Python is in the form of strings. So to convert it into, say float or integer in order to perform different arithmatic operations, you will have to manually typecast it.

age = int(input("Enter the age: "))

if age<5:
    print("Too young to go to school")
elif age>=6 and age<=17:
    print("Go to grade {}".format((age-5)))
elif age==5:
    print("Go to grade 6")
else:
    print("Go to college")