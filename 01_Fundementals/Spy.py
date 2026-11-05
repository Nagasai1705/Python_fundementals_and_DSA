n=int(input("Enter the value: "))
og=n
total=0
product=1
while n!=0:
    x=n%10
    n//=10
    total=total+x

    product=product*x
if total==product:
    print(og,"is a Spy number.")
else:
    print(og,"not a Spy number.")
