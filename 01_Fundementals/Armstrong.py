n=int(input("Enter the vlaue: "))

org=n
count=0
total=0
while n!=0:
    x=n%10
    n=n//10
    count=count+1
n= org
while n!=0:
    x=n%10
    n=n//10
    total=total + x**count

    
if org==total:
    print(org, "is a Armstrong number.")
else:
    print(org,"is not a Armstrong number.")