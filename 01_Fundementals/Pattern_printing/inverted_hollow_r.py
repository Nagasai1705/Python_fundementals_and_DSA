n=5
while n!=0:
    for j in range(1,n+1):
        if n==1 or n==5 or j==1 or j==n:
            print("*", end= " ")
        else:
            print(" ", end= " ")
    print()
    n-=1