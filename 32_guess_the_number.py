import random
num=random.randint(0,30)
guess=int(input("Guess the number:"))
while num!=guess:
    if(guess>num):
        print("higher")
    else:
        print("lower")
        guess=int(input("enter"))
print("you won")
