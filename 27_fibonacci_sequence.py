def recursion(n):
    if(n<=1):
        return n
    else:
        return(recursion(n-1)+recursion(n-2))



num=int(input("enter the number"))
if(num<=0):
    print("Please enter a positive number")
else:
    for i in range(num):
        print(recursion(i))