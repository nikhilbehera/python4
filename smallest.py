numbers = [34, 12, 56, 7, 89, 23]
small = numbers[0]
for nm in numbers:
    if nm < small:
        small = nm

    
print(small)