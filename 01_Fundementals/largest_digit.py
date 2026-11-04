n= int(input("Enter the value:"))
og=0
while n!=0:
    x=n%10
    n=n//10
    if x>og:
        og=x
    
print(og, "is the largest element.")

