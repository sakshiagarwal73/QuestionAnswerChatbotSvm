import bs4 as bs
import urllib.request
import pickle


links = ["https://www.sbi.co.in/portal/web/customer-care/faq-state-bank-vishwa-yatra"]

quest = []
ans = []

for link in links:
    source = urllib.request.urlopen(link).read() #source code

    soup = bs.BeautifulSoup(source,'lxml') #lxml is the parser,converting source to beautiful soup object

    for div in soup.find_all('div',class_='toggle-div-header'): 
        quest.append(str(div.text))

    for paragraph in soup.find_all('span',class_='bolded-txt'):
       paragraph = paragraph.find_parent('p')    
       ans.append(str(paragraph.text))



       
        



file = open('travelcard_ques.txt','wb')
pickle.dump(quest,file)
file.close()

file = open('travelcard_ans.txt','wb')
pickle.dump(ans,file)
file.close()
