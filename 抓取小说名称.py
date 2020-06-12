#
import requests
from pyquery import PyQuery as pq
import xlwt

from fake_useragent import UserAgent
import time
def min1():
    a = 0
    arry = [];
    while a < 1068:
        time.sleep(3)
        a += 1
        print(a)
        url_ = "%s%s%s" % ('http://www.tadu.com/store/98-a-0-5-a-20-p-',a,'-98')
        print(url_)
        proxies = {}
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        req = requests.get(url=url_, headers=headers)
        html = req.text
        doc = pq(html)
        # print(html)
        items = doc('.bookBgList li').items()
        for each in items:
            print(each.find('.bookNm').text())
            arry.append(each.find('.bookNm').text())
    wb = xlwt.Workbook()
    ws = wb.add_sheet('test')
    for index, value in enumerate(arry):
        ws.write(index, 0, value)
    wb.save('./test.xls')


if __name__ == '__main__':
    min1()
