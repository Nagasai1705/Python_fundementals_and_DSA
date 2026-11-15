l=[10,11,11,12,13,14,15,14,12]

d=[]
i=0
while i<len(l):
    
    if l[i] not in d:
        d.append(l[i])
    i+=1 
print(d)
'''for i in l:
        if i not in d:
            d.append(i)
    print(d)'''