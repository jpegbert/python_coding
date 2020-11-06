
"""
字典排序
"""
d = {'a': 1, 'c': 3, 'b': 2}
res = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(res)
print(type(res))
aa = dict(res)
print(aa)
bb = list(aa.keys())
print(bb)
