num1=int(input("ENTER THE NUMBER:"))
num2=int(input("ENTER THE ANOTHER NUMBER:"))

for i in range(max(num1,num2)+1, 1+(num1*num2)):
    if(i%num1==0 and i%num2==0 ):
        lcm=i
        break
print(lcm)
    
