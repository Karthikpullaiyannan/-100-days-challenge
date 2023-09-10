def recursion(n):
    if(n==1):
        return 1
    else:
        return(n*recursion(n-1))

num=int(input("Enter the vale:"))
if(num<0):
    print("Factorial cannot be find for negative numbers")
elif(num==0):
    print("The factorial of 0 is 1")
else:
    print("The factorial of number is",recursion(num))