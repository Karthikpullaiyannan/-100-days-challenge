a=int(input("enter the number"))
b=a
sum=0
while b>0:
    temp=b%10
    sum=sum+temp**3
    b=b//10
if(sum==a):
    print("given number is a armstrong")
else:
    print("it is not a armstrong")
