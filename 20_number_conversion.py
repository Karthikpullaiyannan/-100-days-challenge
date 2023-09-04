print("1.Decimal to Binary \n 2.Decimal to Octal \n 3.Decimal to Hexadecimal")
num=int(input("Enter the option decimal is converted to....."))
if(num==1):
    print("The binary value of the given decimal number is "+ bin(num))
elif(num==2):
    print("The Octal value of the given number is" + oct(num))
else:
    print("The Hexa decimal value of the given number is" + hex(num))
    