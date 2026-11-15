n=[10,10,10,20,30,20,40,20,30,50,30]
freq={ }
for i in n:
    
    if i in freq:
        freq[i] += 1
    else:
        freq[i]=1
print(freq)
for key,value in freq.items():
    if value>1:
        print(key,":",value)
    
    
    


