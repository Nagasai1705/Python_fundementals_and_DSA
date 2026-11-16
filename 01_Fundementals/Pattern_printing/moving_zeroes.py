l=[1, 0, 2, 0, 4, 0, 12]
i=0
j=0
while i<=len(l)-1:
    if l[i]!=0:
        temp=l[i]
        l[i]=l[j]
        l[j]=temp
        i+=1
        j+=1
    else:
        i+=1
print(l)





