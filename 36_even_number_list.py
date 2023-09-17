#list1=[int(list1) for list1 in input("Enter the values in list").split(",")]

list1=[1,2,4,2,24,69,100,32,95,87,103]
print(list1)
even=[]
odd=[]
for i in range(len(list1)):
    num=list1[i]%2
    if(num==0):
        even.append(list1[i])
    else:
        odd.append(list1[i])
print("The Even numbers in list is",even)
print("The Odd numbers in list is",odd)
  
