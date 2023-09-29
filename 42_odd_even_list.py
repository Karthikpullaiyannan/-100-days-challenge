list_1=[int(i) for i in input("Enter the values in list:").split(",")]
odd_list=[]
even_list=[]
for i in list_1:
    if(i%2==0):
        even_list.append(i)
    else:
        odd_list.append(i)
print("Odd list=",odd_list)
print("Even list=",even_list)