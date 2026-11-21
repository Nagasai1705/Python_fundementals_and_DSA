l=[100,4,200,1,26]
values=set(l)
count=0
longest=0
for i in values:
    count=0
    current=i
    if (i-1) not in values:
        while current in values:
            count+=1
            current+=1
        longest=max(count,longest)
print(longest)
