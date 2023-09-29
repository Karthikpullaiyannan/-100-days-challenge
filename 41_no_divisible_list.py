list_1=[int(i) for i in input("Enter the values").split(",")]
num=int(input("Enter the divide number:"))
list_2=[]
print(list_1)
for i in list_1:
    if(i%num==0):
        list_2.append(i)
print(list_2)
