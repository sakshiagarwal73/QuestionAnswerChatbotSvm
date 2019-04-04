import pickle
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

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


listoffiles = ["./data/loan_ques", "./data/netbank_ques",
               "./data/imd_ques", "./data/ppf_ques", "./data/travelcard_ques"]
listwrite = ["./data/loan_p", "./data/netbank_p",
             "./data/imd_p", "./data/ppf_p", "./data/travelcard_p"]

cnt = 0

for f in listoffiles:
    file = open(f, 'rb')
    l = pickle.load(file)
    file.close()

    ans = []
    # print('sdfb')

    for item in l:
        # print(item)
        item = item.lower()
        tokenized = word_tokenize(item)
        wordlist = removestop(tokenized)
        wordlist = lemmatizefun(wordlist)
        wordlist = set(wordlist)
        ans.append(wordlist)

    fl = listwrite[cnt]
    cnt = cnt + 1
    file = open(fl, 'wb')
    pickle.dump(ans, file)
    file.close()


list_file_p = listwrite
list_file_ans = ["./data/loan_ans", "./data/netbank_ans",
                 "./data/imd_ans", "./data/ppf_ans", "./data/travelcard_ans"]

data = []

for i in range(5):
    file = open(list_file_p[i], 'rb')
    file_p = pickle.load(file)
    file.close()

    file = open(list_file_ans[i], 'rb')
    file_ans = pickle.load(file)
    file.close()

    l1 = len(file_p)
    l2 = len(file_ans)

    for j in range(l1):
        data.append([file_p[j], file_ans[j], i+1])

file = open('./data/database', 'wb')
pickle.dump(data, file)
file.close()
