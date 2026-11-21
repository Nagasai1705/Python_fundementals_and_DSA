l=[100,4,200,1,2,3]
values=set(l)
current=1
count=0
longest=0
while current in values:
    count+=1
    current+=1
    longest+=1

print(longest)
