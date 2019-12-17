## In this program, we will see how the main function is used within python. This program will print a list of prime numbers upto the number that the user inputs.

# First, we define a function isPrime that checks if a number is prime or not. If it is prime, then it will return a value True, or else, it will return False.
def isPrime(num):
    for i in range(2,num):
        if i!=num:
            if num%i==0:
                return False
    return True

# Now, we will define another function primeUpto, which will store all the primem numbers upto a given max number inside a list.
def primeUpto(max_num):
    list1=[]
    for i in range(2,max_num+1):
        if isPrime(i)==True:
            list1.append(i)
    print(list1)

# The main function inside a functional program is where we combine and declare all the logical part of our program.
def main():
    max_num= int(input("Enter the number upto which you want the list of primes: "))
    primeUpto(max_num)

# Finally, in the end, initialize the main function to run the program.
main()
