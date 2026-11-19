values=[8,1,4,12,5]

k=len(values)
d={
     
}
for i in range(k):
    for j in range(i+1,k):
        a=values[i]
        b=values[j]
        Tup=(a,b)
         
        difference= abs(a-b)
        
        if difference in d:
            d[difference].append(Tup)

        else:
           d[difference]=[Tup]
    

min_diff=min(d)
print(d[min_diff],":",min_diff)
        

