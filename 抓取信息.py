from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import queue
from selenium.webdriver.common.keys import Keys
import json
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
    # driver.find_element_by_class_name('ag-nav__menu-li')[3].click()

    #
    driver.get("https://ds.appgrowing.cn/leaflet")
    cookies = driver.get_cookies()
    str = '';
    for i in cookies:
        str+="%s=%s;" % (i['name'], i['value'])
    url_ = 'https://ds.appgrowing.cn/api/product/rank?site=&startDate=2020-04-21&endDate=2020-04-27&timeType=range&page=1&limit=20&sort=-quantitySoldIncr&isNew=false&matchType=product'
    header = {
        'cookie': str,
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
    }
    r = requests.get(url=url_, headers=header)
    print(r.text)

if __name__ == "__main__":
    main()
