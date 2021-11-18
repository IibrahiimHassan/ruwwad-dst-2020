n=int(input("enter a number n:"))
fact=1
for i in range(n,0,-1):
    fact=fact*i
    print(i,end= "*")
print()
print("fact of" ,n,"=",fact)

