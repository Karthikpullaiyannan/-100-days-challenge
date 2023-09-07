num1=int(input("ENTER THE NUMBER:"))
num2=int(input("ENTER THE ANOTHER NUMBER:"))
for i in range(1,min(num1,num2)+1):
    if(num1%i==0 and num2%i==0):
        gcd=i
print("The GCD of",num1, "and",num2 ,"is",gcd)