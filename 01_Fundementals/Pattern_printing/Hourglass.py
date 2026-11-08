n=5
for i in range(1,2*n):
    if i<=n:
        for j in range(i):
            print(" ",end=" ")
        for k in range((2*n-2*i)+1):
            print("*",end=" ")
        print()
    if i>n:
        s=2*n-i
        for r in range(s):
            print(" ",end=" ")
        for v in range(2*n-2*s+1):
            print("*", end=" ")
        print()
    
    