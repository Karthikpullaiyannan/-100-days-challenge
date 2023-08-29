a=input("enter the number")
b=input("enetr a number")
c=input("enter a number")
if(a>=b) and (a>=c):
    large=a
elif(b>=a) and (b>=c):
    large=b
else:
    large=c
print("the largest number is ",large)
