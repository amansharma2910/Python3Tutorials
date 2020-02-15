# Here we are going to generate a get integers in the range 0-50, raise each integer to the power 2, and then create a list of integers that are a divisible by 8.

print([i**2 for i in range(50) if i**2 % 8 ==0])

# Multiple for loops in a single list comprehension

print([ x * y for x in range(1,5) for y in range(5,10)])

# Nested list comprehensions. Here, we will generate a list of 100 numbers, multiply each by two and then return a final list of multiples of 8.

print([x for x in [i * 2 for i in range(1,101)] if x % 8 == 0])

# We will generate a list of 50 random integers between 1-1000 and then return a list of integers in the list that are divisible by 9
import random
print([x for x in [random.randint(1,1000) for i in range(50)] if x % 9 == 0])