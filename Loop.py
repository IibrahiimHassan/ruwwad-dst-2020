N=int(input("enter a number N which is lower than 6:"))
i=0
while (i<N):
    number=int(input("enter a number:"))
    i=i+1
    if (number%2==1):
        number=str(number)
print("the odd numbers",N,"are:",number,end=" ""and")
