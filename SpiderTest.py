# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:51:26 2019

@author: IreneXiao
"""
import requests
import time


def get_web_page(url):
    time.sleep(0.5)
    resp = requests.get(
            url=url,cookies={'over18':'1'}
    )
    
    if resp.status_code != 200 :
        print('Invalid url', resp.url)
        return None
    else:
        return resp.text
    

page = get_web_page('https://www.ptt.cc/bbs/Beauty/index.html')
if page :
    print(page)
