samplelist=[8,2,3,0,7]


def sum(samplelist):
    
    for x in samplelist:
        sum=sum+x
    return sum


sum1=sum(samplelist)

print("Expected Output:",sum1)

