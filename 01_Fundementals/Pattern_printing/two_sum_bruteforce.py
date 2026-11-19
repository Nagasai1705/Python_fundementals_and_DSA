values=[1,2,3,4,5]
target=int(input("Enter the value: "))
result=[]
f=len(values)
for i in range(0,f):
    for j in range(i+1,f):
        if values[i]+values[j]==target:
             
            a=(values[i])
            b=(values[j])
            Tup=(a,b)
            result.append(Tup)

if not result:
    print("Invalid value calculation cannot be done!")    
else:
    print(result)
     


