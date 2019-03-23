import pickle
from sklearn.svm import SVC
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.utils import resample

list_file_p =   ["loan_p","netbank_p","imd_p","ppf_p","travelcard_p"]
list_file_ans =   ["loan_ans","netbank_ans","imd_ans","ppf_ans","travelcard_ans"]

data = []

for i in range(5):
    file = open(list_file_p[i],'rb')
    file_p = pickle.load(file)
    file.close()

    file = open(list_file_ans[i],'rb')
    file_ans = pickle.load(file)
    file.close()


    l1 = len(file_p)
    l2 = len(file_ans)
    
    for j in range(l1):
        data.append([file_p[j],file_ans[j],i+1])



file = open('database','wb')
pickle.dump(data,file)
file.close()

unique = []

for item in data:  ## creating vocabulary 
    for word in item[0]:
        if(word not in unique):
            unique.append(word)

            
finalvect = []

for item in data:
    d = {}
    for word in item[0]:
        keys = d.keys()
        if(word not in keys):
            d[word] = 1
        else:
            val = d[word]
            d[word] = val + 1
    vect = [] ## bag of words vector for this question
    for w in unique:
        if(w not in d.keys()):
            vect.append(0)
        else:
            vect.append(d[w])
    finalvect.append(vect)




indexlist = [40,44,18,15,16] ## indexlist contains number of records of each class
sumindex = 0
for i in range(5):
    ansdata = [] ## all records of a particular class , input to bootstraping
    for j in range(indexlist[i]):
        l = []
        l.append(finalvect[j + sumindex])
        l.append(data[j + sumindex][2])    
           
        ansdata.append(l)
    sumindex += indexlist[i]         
    bootdata =  resample(ansdata, replace=True, n_samples= 75, random_state=1)   
    SVC_classifier = SklearnClassifier(SVC())
    SVC_classifier.train(bootdata)    
        
                 





    



    
