numbers = [5, 2, 8, 2, 9]

numbers.append(10)
print(numbers)

numbers.insert(1, 20)
print(numbers)

numbers.extend([30, 40])
print(numbers)

numbers.remove(2)
print(numbers)

numbers.pop()
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

print(numbers.count(2))
print(numbers.index(20))

# output;
# [5, 2, 8, 2, 9, 10]
# [5, 20, 2, 8, 2, 9, 10]
# [5, 20, 2, 8, 2, 9, 10, 30, 40]
# [5, 20, 8, 2, 9, 10, 30, 40]
# [5, 20, 8, 2, 9, 10, 30]
# [2, 5, 8, 9, 10, 20, 30]
# [30, 20, 10, 9, 8, 5, 2]
# 1
# 1