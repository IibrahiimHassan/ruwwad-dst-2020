a=0
positive=0
negative=0
while (a<5):
    number=int(input("enter a number of 5 numbers"))
    if(number>0):
        positive=positive+1
    elif(number<0):
        negative=negative+1
    a=a+1
print("the number of the positive numbers is:",positive)
print("the number of the negative numbers is:",negative)