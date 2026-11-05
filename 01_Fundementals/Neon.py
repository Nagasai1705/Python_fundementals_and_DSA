n= int(input("Enter the value: "))
x= n**2
total=0
while x!=0:
     y=x%10
     x//=10
     total=total+y
print(total)
if n==total:
     print(n,"is a neon number.")
else:
     print(n,"is not a neon number.")