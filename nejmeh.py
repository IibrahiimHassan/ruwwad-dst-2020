for i in range(1,5):
    for j in range(1,5-i):
        print(" ",end="")
    for pls in range(1,i):
        print("+",end="")
    for n in range(1,4):
        print("*",end="")
    print()