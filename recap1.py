L1=[1,2,3,4,5,6,7,8,9,10]
[print("even number is"+" "+str(x)) if x%2==0 else print("Odd number is"+" "+str(x)) for x in L1] 
evens=[x for x in L1 if x%2==0]
print(evens)
(evens, odds) = ([x for x in L1 if x%2==0],[x for x in L1 if x%2!=0])
print(evens)
print(odds)

