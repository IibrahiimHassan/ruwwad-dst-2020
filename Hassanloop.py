import random
x=random.randint(1,100)
c=0
while (c<5):
    a=int(input("guess a number between 1 and 100:"))
    if (a<x):
        print("your guess is less than the solution")
    elif (a>x):
        print("your guess is greather than the solution")
    elif (a==x):
        print(" your guess is equal to the solution")

        print(" you win the game")
        break
    c=c+1
else:
    print(" you loose the game")



