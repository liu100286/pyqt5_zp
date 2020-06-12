import requests, re
from bs4 import BeautifulSoup as bs
import json
from fake_useragent import UserAgent
def get_html(url):
    ua = UserAgent()
    user_agent = ua.random
    header = {'User-Agent':user_agent}
    try:
        r = requests.get(url,headers = header,timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('error,not open page by url:' +url)
def get_proxy_ip(html):
    html = bs(html, 'html.parser')
    proxy_ips = html.find(id='ip_list').find_all('tr')
    for proxy_ip in proxy_ips:
        if len(proxy_ip.select('td')) > 0:
            ip = proxy_ip.select('td')[1].text
            port = proxy_ip.select('td')[2].text
            protocol = proxy_ip.select('td')[5].text
            if protocol in protocollists:
                proxy_ip_list.append(f'{protocol}://{ip}:{port}')
    return proxy_ip_list
def check_proxy_avaliability(ip):
    url = 'https://www.baidu.com'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    headers = {'User-Agent': user_agent}
    try:
        proxies = {}
        if ip.startswith(('HTTPS', 'https')):
            proxies['HTTPS'] = ip
        else:
            proxies['HTTP'] = ip
            print(proxies)
        r = requests.get(url=url, headers=headers, proxies=proxies, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        text, status_code = r.text, r.status_code
        if status_code == 200:
            print('有效IP, %s', ip)
            return True
        else:
            print('无效IP, %s', ip)
            return False
    except:
        print('error  ', url)
        return False


if __name__ == '__main__':
    proxy_ip_list = []
    url = 'https://www.xicidaili.com/'
    protocollists = ['http', 'https', 'HTTP', 'HTTPS']
    html = get_html(url)
    ips = get_proxy_ip(html)
    print(ips)
    use_ip_list = []
    for ip in ips:
        if check_proxy_avaliability(ip):
            use_ip_list.append(ip)
    print('有效代理ip')
    print(use_ip_list)
