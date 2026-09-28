numbers = [10, -5, 20, -8, 15, -3]

result = [0 if x < 0 else x for x in numbers]

print(result)

# ouput;
# [10, 0, 20, 0, 15, 0]