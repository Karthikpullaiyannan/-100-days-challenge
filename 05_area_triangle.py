#Area of Triangle by Heron's formula
a=int(input("enter the base="))
b=int(input("enetr the height="))
c=int(input("enetr the another value"))
s=(a+b+c)/2
e=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of triangle=", float(e))
