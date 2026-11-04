n=int(input("Enter the value: "))
Even_count=0
Odd_count=0
while n!=0:
    x=n%10
    n=n//10
    if x%2==0:
        Even_count=Even_count+1
    else:
        Odd_count=Odd_count+1
print("Even numbers:",Even_count)
print("odd numbers: ",Odd_count)

    