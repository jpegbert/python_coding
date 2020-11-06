import glob


"""
glob模块用于查找符合特定规则的文件路径名。查找文件只用到三个匹配符：" ", "?", "[]"。" "匹配0个或多个字符；
"?"匹配单个字符；"[]"匹配指定范围内的字符，如：[0-9]匹配数字。
"""

"""
glob.glob() 返回所有匹配的文件路径列表。它只有一个参数pathname，定义了文件路径匹配规则
"""
# 获取指定目录下的所有图片
print(glob.glob(r"./*.png"), "\n") # 加上r让字符串不转义
# 获取上级目录的所有.py文件
print(glob.glob(r'./*.py')) # 相对路径

"""
glob.iglob
获取一个可遍历对象，可以逐个获取匹配的文件路径名。与glob.glob()的区别是：glob.glob同时获取所有的匹配路径，而glob.iglob一次只获取一个匹配路径。
"""
f = glob.iglob(r'./*.py')
print(f)
for py in f:
    print(py)
