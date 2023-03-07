#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

url = input('Enter url')

source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')

ingredients = []

for span in soup.find_all('li',class_="wprm-recipe-ingredient"):
    ingredients.append(span.text)



instruction = soup.find('div',class_="wprm-recipe-instruction-group").text

dic = {'Recipe':ingredients,'INSTRUCTIONS':instruction} 



# Directly from dictionary
with open("recipe.json", "w") as outfile:
    json.dump(dic, outfile)

