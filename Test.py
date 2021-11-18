# write a program that ask the user to enter his gender, then enter his age, if his age is above 20 and he is a man, 
# output his age and say" you can play football", if his age is below 20, "he can't play football", otherwise the girl to play basketball.
# write a program that accepts a string of seven characters and calculate the number of digits and letters.
# write a program that calculate the multiplication of the numbers between 10 and 20.

name=input("enter a string of seven characters")
nb=0
letters=0
digits=0

while(nb<len(name)):
    if(name[nb].isalpha()):
        letters=letters+1
    elif(name[nb].isdigit()):
        digits=digits+1
    nb=nb+1
print("the number of letters",letters)
print("the number of digits",digits)    




