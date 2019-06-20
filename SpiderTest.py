# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:51:26 2019

@author: IreneXiao
"""
import requests
import time
from bs4 import BeautifulSoup
import os
import re
import urllib.request
import json

PTT_URL = 'https://www.ptt.cc'

def get_web_page(url):
    time.sleep(0.5)  
    resp = requests.get(
        url=url,
        cookies={'over18': '1'}
    )
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text
    
     
def get_articles(dom, date):
    soup = BeautifulSoup(dom, 'html.parser')
    
    #取得上一頁連結
    paging_div = soup.find('div', 'btn-group btn-group-paging')  
    prev_url = paging_div.find_all('a')[1]['href']
    
    articles = []
    divs = soup.find_all('div','r-ent')  #找到各篇文章
    
    for d in divs:
        if d.find('div','date').string.strip() == date:  #確認日期
            push_count =0
            if d.find('div','nrec').string:  #nrec為推文數
                try:
                    push_count = int(d.find('div','nrec').string)
                except ValueError:
                    pass
            
            if d.find('a'):  #有超連結表示文章還未被刪除
                href = d.find('a')['href']  #取得文章網址
                title = d.find('a').string
                articles.append({
                        'title':title,
                        'href' : href,
                        'push_count' : push_count})
    return articles, prev_url



def parse(dom):
    soup = BeautifulSoup(dom, 'html.parser')
    links = soup.find(id='main-content').find_all('a')
    img_urls = []
    for link in links:
        #判斷圖檔有可能的多種格式，並統一
        if re.match(r'^https?://(i.)?(m.)?imgur.com', link['href']):
            img_urls.append(link['href'])
    return img_urls


def save(img_urls, title):
    if img_urls:
        try:
            dname = title.strip()  # 用 strip() 去除字串前後的空白
            os.makedirs(dname)  #創建資料夾
            for img_url in img_urls:
                if img_url.split('//')[1].startswith('m.'):
                    img_url = img_url.replace('//m.', '//i.')
                if not img_url.split('//')[1].startswith('i.'):
                    img_url = img_url.split('//')[0] + '//i.' + img_url.split('//')[1]
                if not img_url.endswith('.jpg'):
                    img_url += '.jpg'
                fname = img_url.split('/')[-1]
                urllib.request.urlretrieve(img_url, os.path.join(dname, fname))
        except Exception as e:
            print(e)
            
            
if __name__ == '__main__':
    current_page = get_web_page(PTT_URL + '/bbs/Beauty/index.html')
    if current_page:
        articles = []  
        date = time.strftime("%m/%d").lstrip('0')  
        current_articles, prev_url = get_articles(current_page, date)  
        
        while current_articles: #前頁可能也有今日文章
            articles += current_articles
            current_page = get_web_page(PTT_URL + prev_url)
            current_articles, prev_url = get_articles(current_page, date)
       
        for article in articles: #進入各文章
            print('Processing', article)
            page = get_web_page(PTT_URL + article['href'])
            if page:
                img_urls = parse(page)
                save(img_urls, article['title'])
                article['num_image'] = len(img_urls)  
                
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(articles, f, indent=2, sort_keys=True, ensure_ascii=False)
