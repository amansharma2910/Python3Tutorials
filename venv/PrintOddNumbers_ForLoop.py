# In the for loop, we can loop for a list of values, or within a range of values.
# for <variable_name> in [value1, value2,.....]:  - This is the syntax for looping for values within a list. Here, the variable <Variable_name> will one by one take the value of all the values inside the list.
# for for <variable_name> in range(starting_point, ending_point):  - This is the syntax for looping for values within a range. Here, the variable <Variable_name> will one by one take the value of all the values inside the range, begining from the starting point to one value less than the ending point. Alternatively, you can use range(ending_point) to loop from 0.
# Now lets consider an example where we will print all the odd integers from 0 to 20.
print ("The odd numbers between 0-20 is: ", end="")
for i in range(21):
    if i%2!=0:
        print(i, end=" ")
# In the above line, we use 'end="<space>"' to print all the results of for loop in a single line.

# Look stack, binary tree, binary graph, queue, array definitions.