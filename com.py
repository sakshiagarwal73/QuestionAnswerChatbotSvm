import pickle

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
        data.append([file_p[j],file_ans[j],i])



file = open('database','wb')
pickle.dump(data,file)
file.close()


    