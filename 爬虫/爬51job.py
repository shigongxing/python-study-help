import requests
from bs4 import BeautifulSoup
'''
@author: rock
@技术交流: QQ+vx: 940947367
@desc:
'''
headers={
        'UserAgent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }
total=[]
for i in range(1,50):

    url='https://search.51job.com/list/020000%252C070200%252C030200%252C010000,000000,0000,00,9,99,%25E4%25BA%25BA%25E5%25B7%25A5%25E6%2599%25BA%25E8%2583%25BD,2,'+str(i)+'.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    print(url)
    res=requests.get(url)
    res.encoding='gbk'
    #print(res.encoding)
    soup=BeautifulSoup(res.text,'html.parser')
    print(soup)
    posts=soup.select('#resultList > div > p > span > a')
    #print(posts)
    post1=list(map(lambda x:x.text.strip(),posts))
    #print(post1)#获取职位名称
    comps=soup.select('#resultList > div > span.t2 > a')
    comp1=list(map(lambda x:x.text.strip(),comps))
    #print(comp1)#获取公司名称
    areas=soup.select('#resultList > div > span.t3')
    area1=list(map(lambda x:x.text.strip(),areas))
    #print(area1)#获取公司地点
    moneys=soup.select('#resultList > div > span.t4')
    money1=list(map(lambda x:x.text.strip(),moneys))
    #print(money1)#获取薪水
    for post,comp,area,money in zip(post1,comp1,area1,money1):
        total.append({'post':post,'area':area,'money':money})#打包成字典

    import pandas
    deal = pandas.DataFrame(total)
    deal.to_excel('./51job-1.xls')