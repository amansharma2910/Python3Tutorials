# In this program, we will see the use of the ternary operator. What ternary operator does is that it reduces simple if-else statements (not if-elif-else statements) into single, one-line code. It helps in making the code look more clean and short, thus reducing the interpretation time.

age = int(input("Enter your age: "))
can_vote= "Yes, you can vote." if age>=18 else "No, you are too young to vote."

print(can_vote)