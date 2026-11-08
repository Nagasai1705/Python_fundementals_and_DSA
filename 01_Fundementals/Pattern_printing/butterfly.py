n=5
#top half
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    for h in range(2*(n-i)):
        print(" ",end=" ")
    for o in range(i):
        print("*", end=" ")
    print()
#bottom half
for m in range(n-1,0,-1):
    for k in range(m):
        print("*",end=" ")
    for h in range(2*n-2*m):
        print(" ", end=" ")
    for v in range(m):
        print("*",end=" ")
    print()

