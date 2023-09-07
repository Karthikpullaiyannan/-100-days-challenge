def factor(n):
    print("The Factors of" ,n, "are:")
    for i in range(1,n+1):
        if(n%i==0):
            m=i
            
            print(m)    






num=int(input("ENTER A NUMBER:"))
factor(num)