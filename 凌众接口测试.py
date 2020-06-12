# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import json
import queue
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests



def main():
    a = [1]
    z = [];
    for i in a:
        url_="%s=%s;" % ('http://c.lzad.cc/renew_list?per-page=10&page=', i)
        header = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjRmMWcyM2ExMmFhIn0.eyJpc3MiOiJsemFkIiwianRpIjoiNGYxZzIzYTEyYWEiLCJpYXQiOjE1ODgxMzEyMTQsIm5iZiI6MTU4ODEzMTIxNCwiZXhwIjoxNTg4MjE3NjE0LCJ0b2tlbiI6IlNiVWNwWWJIYk12ZDJNWmNuTkl3WXNHX21FTm8tSmp3In0.BIV9IMJQ-eT3zWESGC5NTd40MugWviTk-3i2PJzfFv8',
        }
        r = requests.get(url=url_, headers=header)
        shop = r.text
        # start = json.loads(shop).get('data').get('data')
        # z = z+start
        print(shop)
if __name__ == '__main__':
    main()
