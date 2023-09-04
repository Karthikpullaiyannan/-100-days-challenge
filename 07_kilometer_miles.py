print("1.Kilometer to Miles")
print("2.miles to kilometers")
a=input("Enter your option=")
if(int(a)==1):
    km=float(input("ENTER THE KILOMETERS"))
    miles=km*0.621371
    print("NUMBER OF MILES =",miles)
elif(int(a)==2):
    miles=float(input("ENTER THE MILES"))
    km=miles/0.621371
    print("NUMBER OF KILOMETERS=",km)
else:
    print("PLEASE ENTER A VALID OPTION")
    
    
