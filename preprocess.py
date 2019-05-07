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


def bootstrap(data, finalvect):
    # indexlist contains number of records of each class
    indexlist = [40, 44, 18, 15, 16]
    sumindex = 0
    finalbootdata = []
    oob = []
    for i in range(5):
        ansdata = []  # all records of a particular class , input to bootstraping
        for j in range(indexlist[i]):
            l = []
            l.append(finalvect[j + sumindex])
            l.append(data[j + sumindex][2])

            ansdata.append(l)

        bootdata = resample(ansdata, replace=True,
                            n_samples=75, random_state=1)
        for item in ansdata:
            if item not in bootdata:
                oob.append(item)
        sumindex += indexlist[i]
        for item in bootdata:
            finalbootdata.append(item)

    return finalbootdata


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

def main():
    list_file_ques = ["./data/loan_ques", "./data/netbank_ques",
                "./data/imd_ques", "./data/ppf_ques", "./data/travelcard_ques"]
    list_file_ans = ["./data/loan_ans", "./data/netbank_ans",
                    "./data/imd_ans", "./data/ppf_ans", "./data/travelcard_ans"]

    data = []
    
    for i in range(len(list_file_ques)):
        file = open(list_file_ques[i], 'rb')
        l = pickle.load(file)
        file.close()

        ap = []
        # print('sdfb')

        for item in l:
            # print(item)
            item = item.lower()
            tokenized = word_tokenize(item)
            wordlist = removestop(tokenized)
            wordlist = lemmatizefun(wordlist)
            wordlist = set(wordlist)
            ap.append(wordlist)

        file = open(list_file_ans[i], 'rb')
        file_ans = pickle.load(file)
        file.close()

        for j in range(len(ap)):
            data.append([ap[j], file_ans[j], i+1])


    unique = []

    for item in data:  # creating vocabulary
        for word in item[0]:
            if(word not in unique):
                unique.append(word)

    finalvect = []

    for item in data:
        vect = bagOfWords(unique, item[0])
        finalvect.append(vect)

    finalbootdata = bootstrap(data, finalvect)

    # train the model
    clf = SVC(kernel='rbf')
    x = []
    y = []
    for item in finalbootdata:
        x.append(item[0])
        y.append(item[1])
    clf.fit(x, y)

    file = open('./data/model','wb')
    pickle.dump(clf,file)
    file.close()

    file = open('./data/vocab','wb')
    pickle.dump(unique,file)
    file.close()

    file = open('./data/vectors','wb')
    pickle.dump(finalvect,file)
    file.close()

    file = open('./data/database','wb')
    pickle.dump(data,file)
    file.close()

if __name__ == "__main__":
    main()
