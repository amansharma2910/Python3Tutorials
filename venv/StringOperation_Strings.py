# First we will enter two strings.
string1= input("Enter a string: ")
string2= input("Enter the second string: ")
# Now, we will concatenate(join) those two strings in a third string and then print the result.
string3= string1 + string2
print(string3)

# The len() function is to find out the length of a string.
print("Length of the string = {}".format(len(string1)))

# The type() function is to find out the data type of a variable.
print(type(string1))

# String is basically an array of characters. So we can print the individual characters at a specified index by using the <string name here>[<index number here>].
print(string1[0])
# Character index '-1' prints the last character of the string.
print(string1[-1])

# To print a string from one index to the other, simple use the following syntax- print(<string name here>[<starting index>:<ending index>])
print(string1[0:4])

print(string1[4:])
print("Every other character :", string1[0:-1:2])
print("Reverse :", string1[::-1])

string4= "Hello "
print(string4 * 5)

