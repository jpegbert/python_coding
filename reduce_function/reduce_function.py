from functools import reduce


f = lambda x, y: x + y
res = reduce(f, [1, 2, 3, 4, 5])
print(res) # 15

# 给定初始化值10
res = reduce(f, [1, 2, 3, 4, 5], 10)
print(res) # 25

