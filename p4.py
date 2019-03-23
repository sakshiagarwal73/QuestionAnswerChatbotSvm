import bs4 as bs
import urllib.request
import pickle
import ssl

ssl._create_default_https_context = ssl._create_unverified_context



links = ["https://www.sbi.co.in/portal/web/customer-care/faq-state-bank-vishwa-yatra"]

quest = []
ans = []

for link in links:
    source = urllib.request.urlopen(link).read() #source code

    soup = bs.BeautifulSoup(source,'html.parser') #lxml is the parser,converting source to beautiful soup object

    for paragraph in soup.find_all('span',class_='bolded-txt'):
        
        paragraph = paragraph.find_parent('p')    
        ans.append(str(paragraph.text))
        div = paragraph.find_previous('div')
        div = div.find_previous('div')
        quest.append(str(div.text))

file = open('travelcard_ques','wb')
pickle.dump(quest,file)
file.close()

file = open('travelcard_ans','wb')
pickle.dump(ans,file)
file.close()
