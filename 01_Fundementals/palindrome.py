n= int(input("Enter the value: "))
og=n
sum=0
while n!=0:
    x= n%10
    n=n//10
    sum=sum*10+x

if sum==og:
    print(sum,"is a palindrome.")
else:
    print(sum,"is not a palindrome.")
