from sklearn.feature_extraction.text import CountVectorizer

"""
设置停用词列表，处理中文文档
https://blog.csdn.net/weixin_38278334/article/details/82320307
"""

# 从文件导入停用词表
stpwrdpath = "中文停用词库.txt"
with open(stpwrdpath, 'rb') as fp:
    stopword = fp.read().decode('utf-8')  # 提用词提取
# 将停用词表转换为list
stpwrdlst = stopword.splitlines()
texts = ["dog cat fish", "dog cat cat", "fish bird", 'bird']
# 对CountVectorizer进行初始化（去除中文停用词）
count_vec = CountVectorizer(stop_words=stpwrdlst) # 创建词袋数据结构
X_count_train = count_vec.fit_transform(texts[:2])  # <class 'scipy.sparse.csr.csr_matrix'>
# 将原始训练和测试文本转化为特征向量
X_count_train = X_count_train.toarray()
X_count_test = count_vec.transform(texts[2]).toarray()
print(X_count_train)
# 词汇表
print('\nvocabulary list:\n\n',count_vec.get_feature_names())
print('\nvocabulary dic :\n\n',count_vec.vocabulary_)
print('vocabulary:\n\n')
for key, value in count_vec.vocabulary_.items():
    print(key, value)
