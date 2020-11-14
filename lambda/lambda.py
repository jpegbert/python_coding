
"""
python lambda表达式（又称为匿名函数）
格式：lambda 参数列表:函数体
"""


def add_function(a, b):
    return a + b


def add_lambda(a, b):
    return


if __name__ == '__main__':
    add_function(3, 4) # 以函数的方式实现两数相加
    add_lambda = lambda a, b: a + b # 定义两数相加的lambda方式实现
    add_lambda(3, 4) # 调用lambda方式实现的两数相加
