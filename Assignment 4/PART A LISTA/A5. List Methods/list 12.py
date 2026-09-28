numbers = [1, 2, 2, 3, 4, 4, 5, 1]

unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print(unique)

# output;
# [1, 2, 3, 4, 5]