numbers = [1, 2, 3, 2, 4, 5, 1]
dup = set()
seen = set()
for num in numbers:
    if num in seen:
        dup.add(num)
    else:
        seen.add(num)
print(dup)