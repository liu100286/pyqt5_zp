# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import json
import queue
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import xlwt
import datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def main():
    driver = webdriver.Chrome()
    driver.get("https://youcloud.com/login/appgrowing/")
    driver.find_elements_by_class_name('form-input')[0].click()
    driver.find_elements_by_class_name('form-input')[0].clear()
    driver.find_elements_by_class_name('form-input')[0].send_keys('18510199457')

    driver.find_elements_by_class_name('form-input')[1].click()
    driver.find_elements_by_class_name('form-input')[1].clear()
    driver.find_elements_by_class_name('form-input')[1].send_keys('Wulang#1234')
    driver.find_element_by_class_name('btn-form').click()
    wait = WebDriverWait(driver, 1000)
    wait.until(EC.presence_of_element_located((By.ID, 'ag-youcloud-unit-nav')))
    driver.get("https://ds.appgrowing.cn/leaflet")
    cookies = driver.get_cookies()
    str = '';
    for i in cookies:
        str += "%s=%s;" % (i['name'], i['value'])
    getUrl(str)

def getUrl(str):
    newDate = datetime.datetime.now().strftime("%Y-%m-%d")
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=6)
    n_days = now - delta
    endDate = n_days.strftime('%Y-%m-%d')
    count = 0
    newData = [];
    while (count <= 15):
        time.sleep(2)
        count = count+1
        url_ = "%s%s%s%s%s%s" % ('https://ds.appgrowing.cn/api/product/rank?site=&startDate=', endDate, '&endDate=',
                                 newDate + '&timeType=range&page=', count,
                                 '&limit=20&sort=-quantitySoldIncr&isNew=false&matchType=product')
        header = {
            'cookie': str,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
        }
        r = requests.get(url=url_, headers=header)
        shop = r.text
        start = json.loads(shop).get('data')
        for n in start:
            firstArray = time.localtime(n['firstTime'] / 1000)
            first = time.strftime("%Y--%m--%d %H:%M:%S", firstArray)
            lastArr = time.localtime(n['lastTime'] / 1000)
            last = time.strftime("%Y--%m--%d %H:%M:%S", lastArr)
            da = {
                'finalLink': n['finalLink'],
                'title': n['title']['highlight'],
                'minPrice': n['minPrice'] / 100,
                'maxPrice': n['maxPrice'] / 100,
                'quantitySoldIncr': n['quantitySoldIncr'],
                'quantitySold24HoursIncr': n['quantitySold24HoursIncr'],
                'quantitySold24HoursIncrRatio': n['quantitySold24HoursIncrRatio'],
                'quantitySold12HoursIncr': n['quantitySold12HoursIncr'],
                'quantitySold6HoursIncr': n['quantitySold6HoursIncr'],
                'totalQuantitySold': n['totalQuantitySold'],
                'firstTime': first,
                'lastTime': last,
            }
            newData.append(da)
    xls(newData)
def xls(val):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('test')
    ws.write(0, 0, '地址')
    ws.write(0, 1, '商品')
    ws.write(0, 2, '最小价格')
    ws.write(0, 3, '最大价格')
    ws.write(0, 4, '新增销量')
    ws.write(0, 5, '24h新增销量')
    ws.write(0, 6, '24h增长率')
    ws.write(0, 7, '12h新增销量')
    ws.write(0, 8, '6h新增销量')
    ws.write(0, 9, '累计销量')
    ws.write(0, 10, '销售开始时间')
    ws.write(0, 11, '销售结束时间')
    index = 0
    while index < len(val):
        key = 0;
        index = index + 1
        keys = list(val[index - 1])
        while key < len(keys):
            key = key + 1
            print(key)
            name = val[index - 1][keys[key - 1]];
            ws.write(index, key - 1, name)

    wb.save('./test.xls')
if __name__ == '__main__':
    main()
