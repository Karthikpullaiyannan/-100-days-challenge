def recursion(n):
    if(n<1):
        return n
    else:
        return(n+recursion(n-1))

num=int(input("Enter the value:"))
if(num<0):
    print("Please enter a positive number")
else:
    print(recursion(num))