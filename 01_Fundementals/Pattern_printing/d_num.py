n=int(input("Enter the value: "))
for i in range(0,2*n-1):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(n-(n-i)):
        print(2*k-1,end=" ") 
    print()

''' for v in range(n-(s-1)):
        print(" ",end=" ")
    for o in range(1,s):
        print(o,end=" ")
    print()'''
    

    