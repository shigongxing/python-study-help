#!/usr/bin/env python
# encoding: utf-8
'''
@author: rock
@技术交流: QQ+vx: 940947367
@desc:
'''
import re
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup


def find_date():
    paras = {
        'jl': '北京',  # 搜索城市
        'kw': '人工智能工程师',  # 搜索关键词
        'isadv': 0,  # 是否打开更详细搜索选项
        'isfilter': 1,  # 是否对结果过滤
        'p': 1  # 页数
    }

    url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?' + urlencode(paras)
    print(url)
    p_r = requests.get(url)
    p_c = p_r.text
    print(p_c)
    p_soup = BeautifulSoup(p_c, 'html.parser')
    print(p_soup)
    all = p_soup.find_all('div', {'class':'clearfix'})
    print(all)
    # for item in all:
    #     job_saray = item.find('').find('li', {'class': 'newlist_deatil_two'}).text
    #     print(job_saray)

    pattern = re.compile('职位月薪:(.*?)',re.S)
    # 匹配所有符合条件的内容
    items = re.findall(pattern, str(p_c))
    print(items)



find_date()