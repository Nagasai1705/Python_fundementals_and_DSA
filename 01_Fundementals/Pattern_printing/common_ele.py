n = [1, 2, 2, 8, 9, 4, 5]
b = [2, 2, 5, 6, 8, 9, 9]
r=[]
for i in n:
    for j in b:
        if i==j:
            if i not in r:
                r.append(j)
print(r)
