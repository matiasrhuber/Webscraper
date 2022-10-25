#%%
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import os

# Setup of webdriver
path = os.getcwd()
driver = webdriver.Safari(executable_path = '/usr/bin/safaridriver')
# 
products = []
prices = []
ratings = []
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2")
# Extraction and parsing of page content
content = driver.page_source
print("----------------------------------------------------\ncontent:")
print(content)
soup = BeautifulSoup(content, features='lxml')
print("----------------------------------------------------\nsoup:")
print(soup)
print("----------------------------------------------------\nsoup_list:")
print(soup.find_all('a',href=True, attrs={'class':'_1fQZEK'}))
# for a in 

driver.quit()
# %%
