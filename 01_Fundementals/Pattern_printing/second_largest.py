n =  [-10, -20, -5, -30]

largest=n[0]
second_largest=None
if largest==second_largest:
    largest=n[0]

for i in n:
    if i>largest:
        second_largest=largest
        largest=i
    

    elif second_largest is None or (i>second_largest and i!=largest):
        second_largest=i
        
print(second_largest)

    
    
    