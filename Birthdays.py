birthdays={}
ans="y"
while ans=="y":
    name=input("enter a name:")
    birthday=input("enter a birthday:")

    if name not in birthdays:
        birthdays[name]=birthday
    else:
        print("That entry already exists.")
    print("\nThe birthdays dictionary contains:", birthdays)
    ans=input("\nadd another entry? (y or yes)")
print("\nname \t\t Birthdays")
print("----------------------------------------")
for name in birthdays:
    print(name,"\t\t",birthdays[name])
    
del birthdays["hassan"]
print(birthdays)



