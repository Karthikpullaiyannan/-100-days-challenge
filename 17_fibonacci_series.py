def fibonacci(x):
    if(x<=0):
        return(0)
    elif(x<=1):
        return(1)
    else:
        return(fibonacci(x-1) + fibonacci(x-2))







num=int(input("Enter the number for generating the fibonacci series"))
for i in range(num):
    print(fibonacci(num))