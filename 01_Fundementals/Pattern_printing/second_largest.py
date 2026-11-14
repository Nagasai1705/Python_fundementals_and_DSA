n=[1,12,16,5,26,19]

largest=n[0]
second_largest=n[1]
if largest>second_largest:
    largest=n[0]
else:
    largest=n[1]
for i in n:
    if i>largest:
        second_largest=largest
        largest=i

    elif i>second_largest:
        second_largest=i
        
print(second_largest)

    
    
    