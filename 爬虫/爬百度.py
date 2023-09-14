#!/usr/bin/env python
# encoding: utf-8
'''
@author: rock
@技术交流: QQ+vx: 940947367
@desc:
'''
# coding=utf-8
import requests
import re
from bs4 import BeautifulSoup
def findResult(key,limit=5):
    # 模拟浏览器请求头
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'http://ac.qq.com/Comic/comicInfo/id/540627/Community/topic/topic_id/19598970/page/1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
    }
    search_url='http://www.baidu.com/s?wd=key&rsv_bp=0&rsv_spt=3&rsv_n=2&inputT=6391'
    p_r = requests.get(search_url.replace('key',key),headers=headers)
    p_c = p_r.content
    soup=BeautifulSoup(p_c,"html.parser")
    linkpattern=re.compile("href=\"(.+?)\"")
    div=soup.find('div',id='wrapper').find('div',id='wrapper_wrapper').find('div',id='container').find('div',id='content_left')
    re_dict={}
    for i in range(1,limit):
        a=div.find('div',id=str(i)).find('h3').find('a')
        re_link=linkpattern.findall(str(a))
        re_title=a.text
        re_dict[re_title]=re_link[0]
    for r in re_dict:
        print(r)
        print(re_dict[r])
        print('....................\n')
    return re_dict

# if __name__=='__main__':
# #     while True:
# #         keyword = input("请输入关键字> ").strip()
# #         findResult(keyword)