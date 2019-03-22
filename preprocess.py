import pickle
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize , sent_tokenize
from nltk.stem import WordNetLemmatizer


def removestop(wordlist):
    stop_words = set(stopwords.words("english"))
    ans = []
    for i in wordlist:
        if i not in stop_words:
            ans.append(i)
    return ans

def lemmatizefun(wordlist):
    le = WordNetLemmatizer()
    res = []
    for w in wordlist:
        res.append(le.lemmatize(w))
    return res    

listoffiles = ["loan_ques.txt","netbank_ques.txt","imd_ques.txt","ppf_ques.txt","travelcard_ques.txt"]

for f in listoffiles:
    file = open(f,'rb')
    l = pickle.load(file)
    file.close()

    ans = []



    for item in l:
        
        tokenized = word_tokenize(str(item))
        wordlist = removestop(tokenized)
        wordlist = lemmatizefun(wordlist)
        wordlist = set(wordlist)
        ans.append(wordlist)


    file = open(f,'wb')
    pickle.dump(ans,file)
    file.close()


    
    
    
