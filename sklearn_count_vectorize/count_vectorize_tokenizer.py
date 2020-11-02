from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer
"""
指定分词函数
"""


doc_str_list_train = ["dog cat fish", "dog cat cat", "fish bird", 'bird']
vectorizer = CountVectorizer()
word_tokenizer = vectorizer.build_tokenizer()
doc_terms_list_train = [word_tokenizer(doc_str) for doc_str in doc_str_list_train]
print(doc_terms_list_train)


tokenize = CountVectorizer().build_tokenizer()

def features(document):
    terms = tokenize(document)
    d = {'text_length': len(terms), 'text_spam': whatever_this_means}
    for t in terms:
        d[t] = d.get(t, 0) + 1
    return d

vect = DictVectorizer()
X_train = vect.fit_transform(features(d) for d in documents)
