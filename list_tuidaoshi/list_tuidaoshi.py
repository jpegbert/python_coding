
list1 = [i for i in range(6)]
print(list1) # [0, 1, 2, 3, 4, 5]

list2 = [i + i for i in list1]
print(list2) # [0, 2, 4, 6, 8, 10]

# 有选择的筛选
list3 = [i * i for i in list1 if i > 3]
print(list3) # [16, 25]


