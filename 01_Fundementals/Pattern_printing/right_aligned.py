n=5
while n!=0:
    for i in range(n-1):
        print(" ",end=" ")
    
    for j in range(6-n):
        print("*", end= ' ')
    print()
    n-=1

