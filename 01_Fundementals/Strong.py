n=int(input("Enter the value: "))
original=n


total=0
while n!=0:
    x=n%10
    n//=10
    factorial=1
    i=1
    while i<=x:
        
        factorial=factorial*i
        i+=1
    total= total+ factorial
print(total)
if total==original:
    print(original,"is a strong num.")
else:
    print(original,"is not a strong num.")
