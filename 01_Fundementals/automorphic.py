n= int(input("Enter the value: "))
x=n**2

y=x % 10**(len(str(n)))
if y==n:
    print(n,"is a automorphic num.")
else:
    print(n,"is not a automorphic num.")
