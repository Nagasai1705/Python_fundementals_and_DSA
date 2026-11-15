n=[40,100,30,20,50,25]
largest=n[0]
smallest=n[0]

for i in n:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i


print("largest value:",largest)
print("smallest value:",smallest)

        