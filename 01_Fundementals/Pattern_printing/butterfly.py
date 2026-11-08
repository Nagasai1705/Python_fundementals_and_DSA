n=5
'''#top half
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
    print()'''
for i in range(1,2*n):
    if i<=n:#top half
        for j in range(i):
            print("*",end=" ")
        for l in range(2*n-2*i):
            print(" ",end=" ")
        for o in range(i):
            print("*", end=" ")
    if i>n:#bottom half
        for k in range(2*n-i):
            print("*",end=" ")
        for v in range(2*i-2*n):
            print(" ",end=" ")
        for s in range(2*n-i):
            print("*",end=" ")

            
    print()


