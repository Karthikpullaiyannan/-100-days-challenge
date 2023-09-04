my_list=[22,43,44,65,88,90]
temp=[]
for i in my_list:
    if(i%11 ==0):
        temp.append(i)
print("The numbers divisible by 11 is", temp)
