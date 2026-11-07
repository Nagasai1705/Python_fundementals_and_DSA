n=5 
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(2*i-1):   
        if i==1 or k==0 or k==2*i-2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for r in range(n-1,0,-1):
    
    for l in range(n-r):
        print(" ", end=" ")
    for m in range(2*r-1):
        if m==0 or m==2*r-2:
            print("*", end= " ")
        else:
            print(" ",end=" ")
    print()
