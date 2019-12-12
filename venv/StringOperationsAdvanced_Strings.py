## To remove whitespace, you can use the following string functions-
# lstrip()- This removes whitespace to the left of the string.
# rstrip()- This removes whitespace to the right of the string.
# strip()- This removes whitespace on both sies of the string.

rand_string= "     This is a sample string.   "
rand_string= rand_string.lstrip()
print(rand_string)
rand_string= rand_string.rstrip()
print(rand_string)
rand_string2= "     this is the second sample string.   "
rand_string2= rand_string2.strip()
print(rand_string2)

## Use the following functions to uppercase or lowercase the entire string-
# upper()- This coverts the entire string into uppercase.
# lower()- This converts the entire string into lowercase.
# capitalize()- This capitalizes the first letter of the string.

print(rand_string2.capitalize())
print(rand_string2.upper())
print(rand_string2.lower())

## String operations on a list-
# Use join() to join all the items in a list into a string.
# Use split() to split all the words in a string as list items in a list.

list1= ["This", "is", "a", "sample", "list"]
rand_string3= (" ".join(list1))
print(rand_string3)

list2= rand_string2.split()
for i in list2:
    print(i, end=" ")

## Now, we will see some more  functions that can be performed in strings.
# Use count() to get the number of times a sub-string appears in a string.
# Use find() to get the index of the sub-string in a string.
# Use replace to replace a sub-string with some other sub-string.

print("Number of times \"is\" appears in string 3:", rand_string3.count("is"))
print("Index of \"list\":", rand_string3.find("list"))
print(rand_string3.replace("list", "of how we replace a substring."))
