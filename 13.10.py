
N=int(input("enter the first number N:"))
M=int(input("enter the last number M:"))
i=N
sum=0
print("the sum of:",end=" ")
while (i<M):
    sum=sum+i
    print(i,end="+")
    i=i+1
sum=sum+M

print(M,"=",sum)