from bs4 import BeautifulSoup
import requests
url= "https://cubersindia.com/"


#print(url)

r = requests.get(url)
#print(r)

htmlContent = r.content
#print(htmlContent)

s = BeautifulSoup(htmlContent,"html.parser")
#print(s.prettify)

title = s.title
#print(title)

paras = s.find_all('p')
anchors = s.find_all('a')
#print(para)
#print(anc)
#print(s.find('p')['class'])
#print(s.find('a')['class'])

#print(s.find_all("p",class_="topbar-content"))

all_links = set()
for link in anchors:
    if(link.get('href')!= '#'):
        linkText = link.get('href')
        print(linkText)

com = "<p><!--this is a comment object --></p>"
s2 = BeautifulSoup(com)
print(s2.p.string)

navbar = s.find(id='site-navigation-wrap')
print(navbar.childern)
print(navbar.contents)

for elements in navbar.contents:
    print(elements)

for item in navbar.stripped_strings:
    #print(item)
    print(item)

print(navbar.parent)

print(navbar.parents)

for item in navbar.parents:
    print(item.name)

print(navbar.next_sibling)
print(navbar.next_sibling.next_sibling)

print(navbar.previous_sibling)
print(navbar.previous_sibling.previous_sibling)

abc = s.select('.topbar-content')
print(abc)






























