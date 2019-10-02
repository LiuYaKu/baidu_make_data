# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import os
import re
import pandas as pd

res=open("web_have_word.txt","w",encoding="utf-8")
res_n=open('web_not_have_word.txt',"w",encoding='utf-8')
have_search=set([i.strip() for i in open('have_search',"r",encoding='utf-8')])
driver = webdriver.Chrome()
driver.get('https://baike.baidu.com/')
wordsAndNum = open('new_relu_no_proword.txt', encoding='utf-8')

words = []
for i in wordsAndNum:
    words.append(i.strip())

#hasSearched = []  # 能搜得到的地方对应位置为1 ，否则为0

for index, word in enumerate(words):
    if word in have_search:
        continue
    try:
        element_text = driver.find_element_by_id('query')
        element_text.clear()
        element_text.send_keys(word)
        element_button = driver.find_element_by_id('search')
        element_button.click()
        main_content = driver.find_element_by_class_name('main-content')
        if main_content:
            res.write(word+"\n")
            #hasSearched.append(1)
            print('searched word : {}   index : {}'.format(word, index))
        else:
            res_n.write(word+"\n")
            #hasSearched.append(0)
            print('did not find word : {}   index : {}'.format(word, index))
    except:
        res_n.write(word + "\n")
        #hasSearched.append(0)
        print('bug word : {}   index : {}'.format(word, index))
