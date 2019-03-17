numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers) # [1, 2, 3, 4, 5, 6]

numbers.insert(0, -1)
print(numbers) # [-1, 1, 2, 3, 4, 5, 6]

numbers.remove(6)
print(numbers) # [-1, 1, 2, 3, 4, 5]

numbers.pop(0)
print(numbers) # [1, 2, 3, 4, 5]

numbers.reverse()
print(numbers) # [5, 4, 3, 2, 1]

numbers.sort()
print(numbers) # [1, 2, 3, 4, 5]

print(numbers.index(5)) # 4

second_list = [6, 7, 8]
numbers.extend(second_list)
print(numbers) # [1, 2, 3, 4, 5, 6, 7, 8]