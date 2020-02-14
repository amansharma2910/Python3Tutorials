a = [1,2,3,4]
try:
    print(a[5])
except IndexError:
    print("Sorry but this index doesn't exist in the list.")
    print("Enter an index in the range 0-3.")