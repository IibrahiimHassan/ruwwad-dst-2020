N=int(input("enter a first number N:"))
M=int(input("enter a last number M:"))

sum=0
print("the sum of:",end="")
for a in range(N,M+1):
    sum=sum+a
    print(a,end="+")
print("=",sum)
