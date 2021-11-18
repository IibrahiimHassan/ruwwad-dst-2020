names1=[]
nb_cars=int(input("enter the nb of cars:"))
for i in range(nb_cars):
    car_name=input("enter the name of the car:")
    while car_name in names1:
        car_name=input("Error, duplicate name, enter a new car:")
    else:
        names1.append(car_name)

print(names1)
for i in range(len(names1)):
    print(names1[i],end="-")