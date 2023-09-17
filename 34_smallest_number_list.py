list1=[int(list1) for list1 in input("Enter the values in the list").split(",")]
#method 1
"""
num=list1[0]
for i in range(len(list1)):
    if(list1[i]<num):
        num=list1[i]
    
print(num)"""
print(list1)

#method 2
#print("The smallest number in the list is",min(list1))

#method 3
list1.sort()
print(list1[0])
