
def is_not_none(x):
    return x and len(x.strip()) > 0


list1 = ["", " ", "aaa", "dasd", None, "bsc"]
res = filter(is_not_none, list1)
print(list(res))

