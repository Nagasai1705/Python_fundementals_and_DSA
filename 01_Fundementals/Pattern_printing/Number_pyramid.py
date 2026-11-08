n=5
for i in range(n,0,-1):
    for j in range(i-1):
        print(" ",end=" ")
    for k in range(n-(i-1)):
        print(k+1,end=" ")
    for l in range(k,0,-1):
        print(l,end=" ")
    
    print()
