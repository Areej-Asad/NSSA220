# 13 ex
import requests 
from bs4 import BeautifulSoup 
import pandas as pd 

URL = "https://realpython.github.io/fake-jobs/" 
page = requests.get(URL) 
soup = BeautifulSoup(page.text,"html.parser")  
titles = [t.getText().strip() for t in soup.find_all(class_="title is-5")] 
companies = [ t.getText().strip() for t in soup.find_all(class_="subtitle is-6 company")] 
locations = [ t.getText().strip() for t in soup.find_all(class_="location")] 
dates = [ t.getText().strip() for t in soup.find_all('time')] 
df = pd.DataFrame() 
df['job title'] = titles 
df['company'] = companies 
df['location'] = locations 
df['date'] = dates  

print(df.head())
