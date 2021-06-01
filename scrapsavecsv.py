import pandas as pd
from bs4 import BeautifulSoup
import requests

#url = 'https://www.kite.com/' this website is not able to use for scrap now use next any available site.
url = 'https://islamqa.info/en/answers/1/interruption-of-wudhu'

r = requests.get(url)

htmlContent = r.content
#print(htmlContent)

s = BeautifulSoup(htmlContent,'html.parser')
#print(s)

abc = s.findAll(attrs = {'class' : 'content'})
#print(abc)

abc1 = abc[0].text.replace('\n'," ")
print(abc1)

summary = s.find(attrs = {'class' : 'title is-4 is-size-5-touch'}).text.replace('\n',"")
print(summary)

q1 = int(s.find(attrs = {'class' : 'subtitle has-text-weight-bold has-title-case cursor-pointer tooltip'}).text.replace('\n',""))

source = s.find(attrs = {'class' : 'subtitle is-6 has-text-weight-bold is-capitalized'}).text.replace('\n',"").replace('Source',"")
#print(source)

data = [[url, abc1, summary, q1, source]]
print(data)

df = pd.DataFrame(data, columns = ['url', 'abc1', 'summary', 'q1 #', 'source'])
df.to_csv('vvv.csv')


*********************************
for i in range(1,10):
    url = 'https://islamqa.info/en/latest' +str(i)
    r = requests.get(url)
    if(r.status_code==200):
        print('Status code connected successfully',i)
        s = BeautifulSoup(r.content,'html.parser')
        qna = s.findAll(attrs = {'class':'content'})
        Q = qna[0].text.replace('\n',"")
        A = qna[1].text.replace('\n',"")
        QS = s.find(attrs = {'class':'title is-4 is-size-5-touch'}).text.replace('\n',"")
        qn = int(s.find(attrs = {'class' : 'subtitle has-text-weight-bold has-title-case cursor-pointer tooltip'}).text.replace('\n',""))
        Sorce = s.find(attrs = {'class' : 'subtitle is-6 has-text-weight-bold is-capitalized'}).text.replace('\n',"").replace('Source',"")
        data.insert(qn,[url,qn,QS,Q,A,Sorce])
    else:
        print('URL not working',i)
df = pd.DataFrame(data,columns = ['URL', 'QuestionNo #', 'Question', 'QT', 'source'])
df.to_csv("newdata.csv")