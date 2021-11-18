N=int(input("enter a number N:"))
for a in range (2,N):
    if (N%a==0):
        print("this number isn't prime")
        break
else:
    print("this number is prime")
