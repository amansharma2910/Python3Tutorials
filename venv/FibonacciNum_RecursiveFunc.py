def fibonacci(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        fib = fibonacci(index-1) + fibonacci(index-2)
        return fib

index = int(input("Enter the index upto which you want the fibonacci numbers: "))
for i in range(1,index+1):
    print(fibonacci(i), end=" ")