list1=[int(list1) for list1 in input("Enter the values in list").split(",")]
print(list1)
num=0
for i in list1:
    num=num+i
    averge=num/len(list1)
print("The sum of the list is",num)
print("Average of the list values is",averge)
