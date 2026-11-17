values=[1,2,3,4,5]
Sum = (int(input("Enter the value: ")))
pairs=[]
k=0
for i in values:
    if values[k] not in pairs:
        for j in values:
            if i+j==Sum:
                pairs.append(i)
                pairs.append(j)
        k+=1  
print(pairs)
