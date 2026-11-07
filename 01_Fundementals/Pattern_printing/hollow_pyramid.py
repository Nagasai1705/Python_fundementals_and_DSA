n=5 
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end=" ")
    y=2*i-1
    for k in range(y):
        if i==1 or i==5 or k==0 or k==y-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    