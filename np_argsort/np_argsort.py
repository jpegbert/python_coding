import numpy as np


"""
np.argsort()的用法
函数原型：numpy.argsort(a, axis=-1, kind=’quicksort’, order=None)
功能: 将矩阵a按照axis排序，并返回排序后的下标
参数: a:输入矩阵， axis:需要排序的维度
返回值: 输出排序后的下标
"""


# 对于一维
x = np.array([1, 4, 3, -1, 6, 9])
# argsort()是将X中的元素从小到大排序后，提取对应的索引index，然后输出到y,如x[3]=-1最小，x[5]=9最大
print(x.argsort()) # array([3, 0, 1, 2, 4, 5], dtype=int64)
print(type(x.argsort())) # <class 'numpy.ndarray'>

# 取数组x的最小值
print(x[x.argsort()[0]]) # -1
# 或者用argmin()函数
print(x[x.argmin()]) # -1

# 数组x的最大值, -1代表从后往前反向的索引
print(x[x.argsort()[-1]])  # 9
# 或者用argmax()函数
print(x[x.argmax()]) # 9

# 输出排序后的数组
print(x[x.argsort()]) # [-1  1  3  4  6  9]
# 或
print(x[np.argsort(x)]) # [-1  1  3  4  6  9]


# 二维数组)
x = np.array([[1, 5, 4], [-1, 6, 9]])
# [[ 1  5  4]
# [-1  6  9]]

# 沿着行向下(每列)的元素进行排序
print(np.argsort(x, axis=0))
# array([[1, 0, 0],
#        [0, 1, 1]], dtype=int64)

# 沿着列向右(每行)的元素进行排序
print(np.argsort(x, axis=1))
# array([[0, 2, 1],
#        [0, 1, 2]], dtype=int64)

