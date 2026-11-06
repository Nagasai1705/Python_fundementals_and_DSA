n=int(input("Enter the value: "))
 
og=n
seen=set()
while n!=1 and n not in seen:
    seen.add(n)
    total=0
    while n!=0:
         
        y=n%10
        n//=10
         
        total=total+y**2
    n=total
    
if n==1:   
    print(og,"is a Happy number.")
else:
    print(og, "is not a Happy number.")



