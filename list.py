names=[]
grades=[]
numberofstudents=int(input("how many students in the class:"))
for n in range(numberofstudents):
    name=input("enter a name:")
    grade=float(input("enter a grade:"))
    names.append(name)
    grades.append(grade)

print(names,"\t")
print(grades,"\t")

for i in range(len(names)):
    print(names[i]+"\t",grades[i])

