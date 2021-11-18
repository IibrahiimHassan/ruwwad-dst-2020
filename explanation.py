A=[1,2,3,4,5]
B=[10,9,8,7,5]
C=[]

for i in range(len(A)):
    sum=A[i]+B[-i-1]
    C.append(sum)

print(C)
