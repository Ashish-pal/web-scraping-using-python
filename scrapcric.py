from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sys
import time

url = "https://www.cricbuzz.com/"

#r = requests.get(url)
#print(r)

try:
    r = requests.get(url)
    
except Exception as e:
    
    error_type, error_object, error_info = sys.exc_info()
    print('error for link', url)
    
time.sleep(2)
s = BeautifulSoup(r.text,'html.parser')
links = s.find_all('div', attrs = {'class':'cb-nws-intr'})

for i in links:
    print(i.text)

