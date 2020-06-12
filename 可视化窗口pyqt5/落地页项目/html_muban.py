from PyQt5 import QtCore, QtGui, QtWidgets
from jinja2 import Environment, FileSystemLoader
import os
import re
class get_html_muban(object):
    def settingHtml(self):
        socketIp = self.socketIp
        comboText = self.comboText
        muban_html = 'lp1.html'
        button_data = []
        no_xuanfu = [];
        background_data = []
        mb_num = []
        button_background = [];
        button_button = [];
        env = Environment(loader=FileSystemLoader('./'))
        imgData = self.textEdit_2.toPlainText()
        if imgData != '':
            new_data = "".join((re.sub("\n", " ", imgData)).split(" "))
            str_to_dict = eval(new_data)
        if comboText == '下载按钮悬浮':
            video_img = '';
            videImg = []
            if str_to_dict['video_img'][0] == '视屏背景':
                video_img = '';
            else:
                video_img = str_to_dict['video_img'][0]
                videImg = [{
                    'name': 'video',
                    'img': video_img
                }]
            if str_to_dict['background'][0] == '图片地址':
                return
            for n in str_to_dict['background']:
                background_data.append(n)
            obj = {}
            no_obj = {}
            mb_obj = {}
            for k in str_to_dict['xuanfu']:
                if k != '按钮悬浮图片地址' and k!='':
                    obj = {
                        'name': 'xuanfu',
                        'img': k
                    }
                    button_data.append(obj)
            for j in str_to_dict['no_xuanfu']:
                if j != '按钮不悬浮图片地址' and j!='':
                    no_obj = {
                        'name': 'no_xuanfu',
                        'img': j
                    }
                    no_xuanfu.append(no_obj)
            for z in range(str_to_dict['zhezhao_down']):
                mb_obj = {
                    'name': 'zhezhao_down',
                    'img': ''
                }
                mb_num.append(mb_obj)
            pop={}
            zhezhao_pop = []
            for h in range(str_to_dict['zhezhao_pop']):
                pop = {
                    'name': 'zhezhao_pop',
                    'img': ''
                }
                zhezhao_pop.append(pop)
            newButon = [];

            newButon.extend(button_data)
            newButon.extend(no_xuanfu)
            newButon.extend(mb_num)
            newButon.extend(zhezhao_pop)
            newButon.extend(videImg)
            template = env.get_template('./muban/lp1.html')
            img1 = background_data
            with open(muban_html, 'w+', encoding="utf-8") as fout:
                html_content = template.render(img1=img1, newButon=newButon,socketIp=socketIp)
                fout.write(html_content)
            f = open("lp1.html", "r", encoding="utf-8")  # 读取文件
        elif comboText == '底部下载':
            if str_to_dict['background'][0] == '图片地址':
                return
            video_img = '';
            videImg = []
            if str_to_dict['video_img'][0] == '视屏背景':
                video_img = '';
            else:
                video_img = str_to_dict['video_img'][0]
                videImg = [{
                    'name': 'video',
                    'img': video_img
                }]
            obj = {}
            no_obj = {}
            mb_obj = {}
            for n in str_to_dict['background']:
                background_data.append(n)
            for k in str_to_dict['button_background']:
                button_background.append(k)
            for j in str_to_dict['button']:
                button_button.append(j)
            for f in str_to_dict['no_xuanfu']:
                if f != '按钮不悬浮图片地址':
                    no_obj = {
                        'name': 'no_xuanfu',
                        'img': f
                    }
                    no_xuanfu.append(no_obj)
            for z in range(str_to_dict['zhezhao_down']):
                mb_obj = {
                    'name': 'zhezhao_down',
                    'img': ''
                }
                mb_num.append(mb_obj)
            pop={}
            zhezhao_pop = []
            for h in range(str_to_dict['zhezhao_pop']):
                pop = {
                    'name': 'zhezhao_pop',
                    'img': ''
                }
                zhezhao_pop.append(pop)
            newButon = [];
            newButon.extend(no_xuanfu)
            newButon.extend(mb_num)
            newButon.extend(zhezhao_pop)
            newButon.extend(videImg)
            template = env.get_template('./muban/lp2.html')
            img1 = background_data
            with open(muban_html, 'w+', encoding="utf-8") as fout:
                html_content = template.render(img1=img1, newButon=newButon, button_background=button_background,
                                               button_button=button_button,socketIp=socketIp)
                fout.write(html_content)
            f = open("lp1.html", "r", encoding="utf-8")  # 读取文件
        elif comboText == '底部下载，中间图片横向滑动':
            if str_to_dict['background_top'][0] == '顶部图片地址':
                return
            background_top = [];
            background_slide = [];
            background_bottom = [];
            obj = {}
            no_obj = {}
            mb_obj = {}
            for n in str_to_dict['background_top']:
                background_top.append(n)
            for n in str_to_dict['background_slide']:
                background_slide.append(n)
            for n in str_to_dict['background_bottom']:
                background_bottom.append(n)
            for k in str_to_dict['button_background']:
                button_background.append(k)
            for j in str_to_dict['button']:
                button_button.append(j)
            for f in str_to_dict['no_xuanfu']:
                if f != '按钮不悬浮图片地址':
                    no_obj = {
                        'name': 'no_xuanfu',
                        'img': f
                    }
                    no_xuanfu.append(no_obj)
            for z in range(str_to_dict['zhezhao']):
                mb_obj = {
                    'name': 'zhezhao',
                    'img': ''
                }
                mb_num.append(mb_obj)
            newButon = [];
            newButon.extend(no_xuanfu)
            newButon.extend(mb_num)
            template = env.get_template('./muban/lp3.html')
            with open(muban_html, 'w+', encoding="utf-8") as fout:
                html_content = template.render(background_top=background_top,background_slide=background_slide,background_bottom=background_bottom,newButon=newButon, button_background=button_background,
                                               button_button=button_button,socketIp=socketIp)
                fout.write(html_content)
            f = open("lp1.html", "r", encoding="utf-8")  # 读取文件
        elif comboText == '底部下载，中间图片轮播':
            if str_to_dict['background_top'][0] == '顶部图片地址':
                return
            background_top = [];
            background_slide = [];
            background_bottom = [];
            obj = {}
            no_obj = {}
            mb_obj = {}
            for n in str_to_dict['background_top']:
                background_top.append(n)
            for n in str_to_dict['background_slide']:
                background_slide.append(n)
            for n in str_to_dict['background_bottom']:
                background_bottom.append(n)
            for k in str_to_dict['button_background']:
                button_background.append(k)
            for j in str_to_dict['button']:
                button_button.append(j)
            for f in str_to_dict['no_xuanfu']:
                if f != '按钮不悬浮图片地址':
                    no_obj = {
                        'name': 'no_xuanfu',
                        'img': f
                    }
                    no_xuanfu.append(no_obj)
            for z in range(str_to_dict['zhezhao']):
                mb_obj = {
                    'name': 'zhezhao',
                    'img': ''
                }
                mb_num.append(mb_obj)
            newButon = [];
            newButon.extend(no_xuanfu)
            newButon.extend(mb_num)
            template = env.get_template('./muban/lp4.html')
            with open(muban_html, 'w+', encoding="utf-8") as fout:
                html_content = template.render(background_top=background_top, background_slide=background_slide,
                                               background_bottom=background_bottom, newButon=newButon,
                                               button_background=button_background,
                                               button_button=button_button,socketIp=socketIp)
                fout.write(html_content)
            f = open("lp1.html", "r", encoding="utf-8")  # 读取文件
        elif  comboText == '全屏无缝滚动':
            if str_to_dict['background_slide'][0] == '轮播图片':
                return

            background_slide = [];
            down_img = [];
            xuanfu_img = [];
            background_slide = str_to_dict['background_slide'][0]

            down = {};
            for n in str_to_dict['down_img']:
                down = {
                    'name':'xiazai',
                    'img':n
                }
                down_img.append(down)
            no_down = {}
            for n in str_to_dict['xuanfu']:
                no_down = {
                    'name':'no_xiazai',
                    'img':n
                }
                xuanfu_img.append(no_down)

            template = env.get_template('./muban/lp6.html')
            newButon = [];
            newButon.extend(down_img)
            newButon.extend(xuanfu_img)
            with open(muban_html, 'w+', encoding="utf-8") as fout:
                html_content = template.render(background_slide=background_slide, newButon=newButon,socketIp=socketIp)
                fout.write(html_content)
            f = open("lp1.html", "r", encoding="utf-8")  # 读取文件
        f = f.read()
        self.browser.setHtml(f)
