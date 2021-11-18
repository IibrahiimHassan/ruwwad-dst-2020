set1={"Java","Python","Javascript","C ++","C #"}
set2={"VB.ET","Java","Kotlin","Python"}
set3={}
def intersection(set1,set2):
    set3={x for x in set1 if (x in set2)}
    return set3

set5=intersection(set1,set2)
print(set5)

