n= int(input("Enter the value: "))
total=0

for i in range(1,n):
    x=n%i
    if x==0:
        total= total+i
print(total)
if total==n:
    print(n,"is a perfect num.")
else:
    print(n,"is not a perfect num.")


        