n=int(input("Enter the value: "))
prev=[]
for i in range(1,n+1):
    if i==1:
        current=[1]
    elif i==2:
        current=[1,1]
    else:
        prev= current.copy()
        current.clear()
        current.append(1)
        for k in range(0,len(prev)-1):
            current.append(prev[k]+prev[k+1])
        current.append(1)

    print(" "*(n-i),end=" ")
    for j in current:
        print(j,end=" ")

    print()
    


