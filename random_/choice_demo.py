# from random import choice
import random

# random.choice每次随机返回一个元素
print("choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9]))
print("choice('A String') : ", random.choice('A String'))

# random.sample可以设置每次随机多个元素
print("random.sample([1, 2, 3, 5, 9], 3): ", random.sample([1, 2, 3, 5, 9], 3))
