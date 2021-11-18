n=int(input("enter N:"))
names=""
for i in range(1,n+1):
    name=input("enter a name"+str(i)+":")
    names=names + name + " \n"
    i=i+1
print(names)