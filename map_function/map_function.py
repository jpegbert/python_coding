
list1 = [1, 2, 3, 4, 5]
r = map(lambda x: x + x, list1)
print(list(r)) # [2, 4, 6, 8, 10]

# map传多个参数
r1 = map(lambda x, y: x * x + y, [1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
print(list(r1)) # [3, 8, 15, 24, 35]
