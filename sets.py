# write a program that ask the user to define a set of 
#1. add three elements to the set
#2.print the elements of this set
#3.update the set with two new elements from a list
#4.ask the user to remove N elements from the set
#5.ask the user wether he wants to clear or remove the set
set={"hassan","mahmoud","samir","jaafar",}
set1={"taty","koky"}
list=["samira","khadra"]
set.add("farid")
set.add("fadi")
set.add("fadia")
print(set)
set.update(list)
print(set)
N=int(input("how many elements do you want to remove:"))
for i in range(N):
    set.pop()
print("after pop:",set)

set2=set.union(set1)
print(set2)

opinion=input(" do you want to clear or remove the set:")
if opinion=="yes":
    set.clear()
    print(set)
else:
    del set
    print(set)

