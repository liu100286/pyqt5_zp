import requests
import re
from PIL import Image
#厦大选课url
url = 'https://cas.baidu.com/?tpl=www2&fromu=http%3A%2F%2Fwww2.baidu.com%2Fcommon%2Fappinit.ajax'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/55.0.2883.103 Safari/537.36', 'Connection':'keep-alive'}
#定义一个session()的对象实体s来储存cookie
s =requests.session()

response1 = s.get(url=url, headers=headers)
response1.encoding = 'utf-8'
html1 = response1.text
#利用正则表达式找到验证码的url，由于得到的是列表，用list[0]转成str
cheakcode_url = re.findall(r'<img\s*src="(.*?)"\s*width="80px"\s*height="20px"',html1)[0]
print(cheakcode_url)
# response2 = s.get(url=cheakcode_url, headers=headers)
# #在当前文件夹保存为code.jpg，注意要用'b'的二进制写的方式，用content来获得bytes格式
# with open('code.jpg','wb') as fp:
#     fp.write(response2.content)
# #打开并显示图片
# img=Image.open('code.jpg')
# img.show()
# #需要给服务端传送的数据，字典格式
# data = {}
# data['username'] = '123'
# data['password'] = '123'
# data['checkCode'] = input('输入验证码：')
# response3 = s.post(url=url, data=data, headers=headers)
# print(response3.text)