#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import requests
import bs4
import fastnumbers
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import json
#from tidylib import tidy_document # for tidying incorrect html

sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# In[194]:


############ To get Ticker List ################
data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
table = data[0]
sliced_table = table[1:]
header = table.iloc[0]
corrected_table = sliced_table.rename(columns=header)
company_List = ['3M Company','Adobe Systems Inc','Allstate Corp','Amazon.com Inc.','Apple Inc.','American Express Co','JPMorgan Chase & Co.','Visa Inc.','Xilinx','Facebook, Inc.']
corrected_table = corrected_table[corrected_table.Security.isin(company_List)]
#print(len(company_List))
#corrected_table
tickers = corrected_table['Symbol'].tolist()
print (tickers)
s,s2 = 'https://www.worldtradingdata.com/api/v1/stock?symbol=','https://www.worldtradingdata.com/api/v1/stock?symbol='
for i in range(0,len(tickers)-7):
    s = s + tickers[i] + ','
s = s + tickers[len(tickers)-6] + '&api_token=p4nU2OENDDJfkKP6TePnfKAgI4W5sz2GQmsVBehWiAjwLN6srpgbqp8lfiaV'
s
for i in range(len(tickers)-5,len(tickers)-1):
    s2 = s2 + tickers[i] + ','
s2 = s2 + tickers[-1] + '&api_token=p4nU2OENDDJfkKP6TePnfKAgI4W5sz2GQmsVBehWiAjwLN6srpgbqp8lfiaV'
s2


# In[196]:


################# Call get method to take response from URL ###################

#response = requests.get("https://www.worldtradingdata.com/api/v1/stock?symbol=AAPL,MSFT,HSBA.L&api_token=demo", timeout=240)
response = requests.get(s, timeout=240)
response2 = requests.get(s2, timeout=240)
#response.status_code
response.content
response2.content


# In[205]:


############### Convert the content to json ################
content = response.json()
content2 = response2.json()
#content.keys()
#content = content['data']
#type(content)
#content = json.dumps(content)
keys = content['data'][0].keys()
keys2 = content2['data'][0].keys()
#keys
content['data']
content2['data']


# In[203]:


### Witing JSON data into CSV ##################
csvwriter = csv.writer(first_csv)
with open('D:\sum\Its Study Time\Academic\M.S\Spring_2019\Machine Learning\Project\Sumedh_Work\\first_csv.csv', 'a', newline='') as first_csv:
    csvwriter = csv.DictWriter(first_csv, keys,extrasaction='ignore')
    #csvwriter.writeheader()
    csvwriter.writerows(content['data'])
    csvwriter.writerows(content2['data'])


# In[5]:


############# Play using pandas ################
data = pd.read_csv('D:\sum\Its Study Time\Academic\M.S\Spring_2019\Machine Learning\Project\Sumedh_Work\\first_csv.csv')
#data.head
#data.drop()
data.shape

