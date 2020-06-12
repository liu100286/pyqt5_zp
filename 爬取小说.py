import requests
from pyquery import PyQuery as pq
import os,sys
from Cache import Downloader
from Cache import DiskCache
os.chdir('D:/爬虫数据')
def book():
    url = 'https://www.qtshu.com/zetianji/'
    req = requests.get(url=url)
    req.encoding = 'utf-8'
    html = req.text
    doc=pq(html)
    items = doc('.booklist ul li').items()
    # m和index是为了计算下载进度
    m = len(doc('.booklist ul li'))
    fr = open('择天记.txt', 'w')
    index = 1
    for each in items:
        title = each.text()
        url = each.find('a').attr('href')
        # print(title, url)
        if(url):
            index+=1
            url = 'https://www.qtshu.com/zetianji/'+url
            text = Text(url)
            fr.write(title)
            fr.write('\n\n')
            fr.write('text')
            fr.write('\n\n')
            print('已下载:%.3f%%' % float(index / m) + '\r')
            # print(url)
def Text(url):
    html = D(url)
    doc = pq(html)
    item = doc('.contentbox p').text()
    if '\ufeff' in item:
        item = item.replace('\ufeff', '')
    if '\xa0' in item:
        item = item.replace('\xa0', '')
    if '\u30fb' in item:
        item = item.replace('\u30fb', '')
    if '\ufffd' in item:
        item = item.replace('\ufffd', '')
    return item


if __name__ == '__main__':
    cache = DiskCache()
    D = Downloader(cache)
    book()
