import requests
from pyquery import PyQuery as pq
import os,sys
os.chdir('D:/爬虫数据')
def book():
    url = 'https://www.biqukan.com/46381_46381588/'
    url = requests.get(url)
    url.encoding = 'gbk'
    html = url.text
    doc = pq(html)
    items = doc('dd').items()
    H = 'https://www.biqukan.com/'
    fr = open('我的亡灵改造器.txt', 'w',encoding='utf-8')
    k = 0
    for i,data in enumerate(items):
        title = data.text()
        if (title.find('第一章')>=0):
            k=i
        if k > 0:
             href = data.find('a').attr('href')
             if (href):
                 u = H + href
                 fr.write(title)
                 fr.write('\n\n')
                 text1 = text(u)
                 fr.write(text1)
                 fr.write('\n\n')
                 n = len(doc('dd'))
                 print(title)


def text(val):
    url1 = requests.get(val)
    url1.encoding = 'gbk'
    html1 = url1.text
    doc = pq(html1)
    i = doc('.showtxt')
    i.remove('div')
    i.remove('script')
    text1 = i.text()
    return text1
if __name__ == '__main__':
    book()