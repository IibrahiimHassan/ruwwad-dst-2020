H="hen"
Farm={"Cats":10,"Dogs":7,"Cows":5,"Horses":1}
print("the number of cats is:",Farm["Cats"])
print(Farm.keys())
if H in Farm:
    print("Yes there is a hen in the farm")
else:
    print("No it is not exist")

Farm["Dogs"]=Farm["Dogs"]+2
print(Farm)

Farm["rabbit"]=1
print(Farm)

del Farm["Horses"]
print(Farm)

print("The total number of animals in the farm:",sum(Farm.values()))
n1=max(Farm.values())
print("the maximum number in the Farm is: ",n1)

for x in Farm:
    if Farm[x]==n1:
        print("The element that is the most existing:",x)

for x in Farm.keys():
    print(x,end=" ")
print("\n")

for x in Farm.values():
    print(x,end=" ")
