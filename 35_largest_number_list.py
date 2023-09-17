list1=[int(list1) for list1 in input("Enter the values for list").split(",")]
print(list1)
maxi=list1[0]
for i in range(len(list1)):
    if(list1[i]>maxi):
        maxi=list1[i]
print(maxi)
