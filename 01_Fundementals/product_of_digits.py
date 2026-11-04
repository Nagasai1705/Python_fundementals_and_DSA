n=int(input("Enter the value: "))
prod=1
while n!=0:
    x=n%10
    n=n//10
    prod=prod*x
print(prod)
