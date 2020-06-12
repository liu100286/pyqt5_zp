import datetime
import time
import requests
def getUrl():
    str = '_ga=GA1.2.1316760864.1587890958; _gid=GA1.2.728804813.1587890958; YC_NPS_Dialog=true; _gat_gtag_UA_4002880_19=1; AG_Token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2MiOjIzMzkwNiwiZXhwIjoxNTkwNjQzMjgzLCJpYXQiOjE1ODgwNTEyODQsImlkIjoiZWM5Y2QyMTQtMGVlYS0zMjgxLTkyMWYtZWMyZTdiZjI3NjIxIn0.SZZRCGSgTWIlALI6AD7aIUzWM_P71KKo2fcq2bWT7C8; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22233906%22%2C%22%24device_id%22%3A%22171b5ad2d9185-06356454f56723-6373664-1049088-171b5ad2d92397%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fyoucloud.com%2Flogin%2Fappgrowing%2F%22%2C%22%24latest_referrer_host%22%3A%22youcloud.com%22%7D%2C%22first_id%22%3A%22171b5ad2d9185-06356454f56723-6373664-1049088-171b5ad2d92397%22%7D'
    newDate = datetime.datetime.now().strftime("%Y-%m-%d")
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=6)
    n_days = now - delta
    endDate = n_days.strftime('%Y-%m-%d')
    count = 0
    newData = [];
    while (count < 1):
        count = count+1
        url_ = "%s%s%s%s%s%s" % ('https://ds.appgrowing.cn/api/product/rank?site=&startDate=', endDate, '&endDate=',
                                 newDate + '&timeType=range&page=', count,
                                 '&limit=20&sort=-quantitySoldIncr&isNew=false&matchType=product')
        print(url_)
        header = {
            'cookie': str,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
        }
        r = requests.get(url=url_, headers=header)
        shop = r.text
        print(shop)
        start = json.loads(shop)
        print(start)
        for n in start:
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
                'firstTime':datetime.datetime.fromtimestamp(n['firstTime']/1000),
                'lastTime': datetime.datetime.fromtimestamp(n['lastTime']/1000),
            }
            newData.append(da)
    print(newData)
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
            print(name)
            ws.write(index, key - 1, name)

    wb.save('./test.xls')
if __name__ == '__main__':
    getUrl()