n= int(input("Enter the value: "))
original=n
total=0
l=len(str(n))
while n!=0:
    x=n%10
    n//=10
    total=total+x**l
    l=l-1
print("total:",total)
if total==original:
    print(original,"is a Disarium num.")
else:
    print(original,"is not a Disarium num.")

