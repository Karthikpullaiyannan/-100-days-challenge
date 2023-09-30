num_1=int(input("Enter the number of rows"))
num_2=int(input("Enter the number of column"))
a=[]
for i in range(1,num_1+1):
    b=[]
    for j in range(1,num_2+1):
        b.append(input("Enter"))
    a.append(b)  
for i in range(num_1):
    for j in range(num_2):
        print(a[i][j],end=" ")
    print()