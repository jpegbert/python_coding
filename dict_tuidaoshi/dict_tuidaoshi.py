
dict1 = {
    "aa": "11",
    "bb": "22",
    "cc": "33"
}

key = [key for key, val in dict1.items()]
print(key) # ['aa', 'bb', 'cc']

key = [key + "--" for key, val in dict1.items()]
print(key) # ['aa--', 'bb--', 'cc--']

# 只选择符合条件的值
key = [key for key, val in dict1.items() if key == "bb"]
print(key) # ['bb']
