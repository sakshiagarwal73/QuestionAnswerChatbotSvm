import pickle
from sklearn.svm import SVC
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.utils import resample
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
import numpy as np

stop_words = set(stopwords.words("english"))
stop_words.add('?')
stop_words.add('q.')
stop_words.add('a.')
stop_words.add('.')
stop_words.add('\'s')
stop_words.add(',')
stop_words.add(':')
stop_words.add('@')
stop_words.add('#')
#stop_words = set(stopwords)


def removestop(wordlist):

    ans = []
    for i in wordlist:
        if i not in stop_words:
            ans.append(i)
    return ans


def lemmatizefun(wordlist):
    le = WordNetLemmatizer()
    res = []
    for w in wordlist:
        # print(w)
        res.append(le.lemmatize(w))

    # print(res)
    return res


def bagOfWords(vocabulary, item):
    d = {}
    for word in item:
        keys = d.keys()
        if(word not in keys):
            d[word] = 1
        else:
            val = d[word]
            d[word] = val + 1
    vect = []  # bag of words vector for this question
    for w in vocabulary:
        if(w not in d.keys()):
            vect.append(0)
        else:
            vect.append(d[w])
    return vect


def cosine(a, b):
    ma = np.linalg.norm(a)
    mb = np.linalg.norm(b)

    return np.dot(a, b)/(ma*mb)


def main():
    #print('sdf')

    file = open('./../data/database','rb')
    data = pickle.load(file)
    file.close()

    file = open('./../data/vocab', 'rb')
    vocabulary = pickle.load(file)
    file.close()
    
    file = open('./../data/model','rb')
    model = pickle.load(file)
    file.close()

    file = open('./../data/vectors','rb')
    vectors = pickle.load(file)
    file.close()
    
    indexlist = [40, 44, 18, 15, 16]
    prefixList = [0, 40, 84, 102, 117]

    print('sdf')
    inp = str(input())
    item = inp.lower()
    tokenized = word_tokenize(item)
    wordlist = removestop(tokenized)
    wordlist = lemmatizefun(wordlist)
    wordlist = set(wordlist)
    item = bagOfWords(vocabulary, wordlist)
    item = np.array(item)
    item = item.reshape(1, -1)
    class_predicted = model.predict(item)
    class_predicted = class_predicted-1
    #print(class_predicted[0])
    c = indexlist[class_predicted[0]]
    c1 = prefixList[class_predicted[0]]
    min = 0
    min_index = 150
    for i in range(c):
        cosine(item, vectors[i+c1])
        if cosine(item, vectors[i+c1]) > min:
            min = cosine(item, vectors[i+c1])
            #print(min)
            min_index = i+c1
    #print(min_index)
    print(data[min_index][1])


if __name__ == "__main__":
    main()

# tx = []
# ty = []

# for item in oob:
#     tx.append(item[0])
#     ty.append(item[1])

# oy = clf.predict(finalvect)

# incorrect_count=0

# for i in range(len(data)):
#     print(oy[i],data[i][2])
#     if oy[i]!=data[i][2]:
#         incorrect_count+=1

# print(incorrect_count)
