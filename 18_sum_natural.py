nat_ural=int(input("Enter the natural number"))
if(nat_ural<=0):
    print("Please enter a positive number")
elif(nat_ural==1):
    print("The sum of natural  umber is " + 1)
else:
    for i in range(nat_ural):
        i=i+nat_ural
        nat_ural -= 1
    print("The sum of natural numbers is" + i)
    