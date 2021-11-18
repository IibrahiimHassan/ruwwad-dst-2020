import random
randlist=[]
sum=0
count=0
average=0
evennumbers=0

for i in range(10):
    x=random.randint(1,100)
    randlist.append(x)

print(randlist)
max=randlist[0]
min=randlist[0]

for i in randlist:
    sum=i+sum
    count=count+1
average=sum/count
print("the average is:",average)


for j in randlist:
    if j>max:
        max=j
    elif j<min:
        min=j
print("the max is :",max)
print("the min is:",min)

for i in randlist:
    if i%2==0:
        evennumbers=evennumbers+1
print("the number of even numbers is:",evennumbers)

k=0
tries=5
correct_guesses=0
while (tries>0):
    user_guess=(input("Guess a number:"))

    while (not user_guess.isdigit()):
        user_guess=input("please, enter a valid number:")
    
    user_guess=int(user_guess)

    if user_guess in randlist:
        correct_guesses=correct_guesses+1

        while( user_guess in randlist):
            randlist.remove(user_guess)
    
    




