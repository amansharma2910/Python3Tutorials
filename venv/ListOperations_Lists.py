## Given below is the example of how you initialize the list.
my_list= [5,2,9,1]

# The len() method gives us the length of the list.
print("Length:{}".format(len(my_list)))

# We an refer to a particular element within the list by specifying its index number. For example-
print("1st Index:{}".format(my_list[0]))

# We can also refer to elements that fall within a range within the list. See how that's done in the example below.
print("1st 3 Values:{}".format(my_list[0:3]))

# Use  (<element> in <name_of_list>) to check whether an element is within a list or not.
print("9 in List:{}".format(9 in my_list))

# USe index(<element>) method to check for an element within a list.
print("Index for 2:{}".format(my_list.index(2)))

# Use count(<element>) method to check for an element within a list.
print("How Many 2s:{}".format(my_list.count(2)))
# Use remove to remove an element from the list.
my_list.remove(1)
my_list.pop(0)
# Use insert(index_of_location, value_of_element) to insert an element at a specific index in the list.
my_list.insert(0,10)

# Use sort() method to sort the entire list in ascending order.
my_list.sort()
print("Sorted :",my_list)

# Use reverse() method to arrange the entire list in descending order.
my_list.reverse()
print("Sorted :",my_list)
