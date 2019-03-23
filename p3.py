import bs4 as bs
import urllib.request
import pickle
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


links = ["https://www.sbi.co.in/portal/web/customer-care/faq-public-provident-fund"]

quest = []
ans = []

for link in links:
    source = urllib.request.urlopen(link).read() #source code

    soup = bs.BeautifulSoup(source,'html.parser') #lxml is the parser,converting source to beautiful soup object

    for div in soup.find_all('div',class_='toggle-div-header'): 
        quest.append(str(div.text))
        paragraph = div.find_next('div')    
        ans.append(str(paragraph.text))

file = open('ppf_ques','wb')
pickle.dump(quest,file)
file.close()

file = open('ppf_ans','wb')
pickle.dump(ans,file)
file.close()
