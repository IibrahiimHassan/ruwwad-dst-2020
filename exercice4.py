i=0
evennumbers=0
oddnumbers=0
while (i<5):
    number=int(input("enter a number"))
    if (number%2==0):
        print("the number is even")
        evennumbers=evennumbers+1
    elif(number%2==1):
        print("the number is odd")
        oddnumbers=oddnumbers+1
    i=i+1
print("even numbers are:",evennumbers)
print("odd numbers are:",oddnumbers)