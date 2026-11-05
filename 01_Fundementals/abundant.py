n= int(input("enter the value: "))
original=n
total=0
for i in range(1,n):
    x=n%i
    if x==0:
        total=total+i
'''
if total < original:
        print(original,"is an deficient num.")
else:
        print(original,"is not an deficient num.")'''

if total > original:
        print(original,"is an abundant num.")
else:
        print(original,"is not an abundant num.")

