from PyQt5 import QtCore, QtGui, QtWidgets
lp_2020_path = 'C:\\Users\\Administrator\\Desktop\\lz_git\\\lp_2020'
from jinja2 import Environment, FileSystemLoader
landpage_static_path = 'C:\\Users\\Administrator\\Desktop\\lz_git\\landpage_static'
import json
import os
import re
import requests
class get_add_html(object):
    # --------------------------------------创建html
    def getHtml(self):
        get_add_html.add_html(self)
    def add_html(self):
        comboText = self.comboText
        if comboText == '':
            QtWidgets.QMessageBox.about(self, '提示', "请输入文件名称")
            return
        tex = os.access('./indor.txt', os.F_OK)
        url = self.lineEdit.text()
        btn1_text = self.radioButton.text()
        btn1_true = self.radioButton.isChecked()
        btn2_text = self.radioButton_2.text()
        btn2_true = self.radioButton_2.isChecked()
        hrml_path = self.lineEdit_2.text()
        url = url.strip()
        hrml_path = hrml_path.strip()
        if hrml_path == '':
            return
        buttonType = self.buttonType
        path_2020_html = "%s%s%s%s%s%s" % (lp_2020_path, '\\', url, '\\', hrml_path, '.html')
        # 判断问价是否存在老的落地页
        path_landpage_html = "%s%s%s%s%s%s" % (landpage_static_path, '\\', url, '\\', hrml_path, '.html')
        is_landpage_true = os.access(path_landpage_html, os.F_OK)
        buttonCss = ''
        if buttonType != '无':
            hrefCss = "%s%s%s" % ('./html/', buttonType, '.css',)
            with open(hrefCss, 'r') as f:
                buttonCss = f.read()
        if is_landpage_true:
            QtWidgets.QMessageBox.about(self, '提示', "新建改文件已在老落地页项目中存在")
            return
        # 判断新建文件是否存在
        is_true = os.access(path_2020_html, os.F_OK)
        if not is_true:
            banquan = '';
            if self.radio_name == '':
                QtWidgets.QMessageBox.about(self, '提示', "请选择版权")
                return
            elif self.radio_name == '智道未来':
                banquan = 'zhidaoweilai'
            elif self.radio_name == '智鸟':
                banquan = 'zhiniao'
            elif self.radio_name == '无版权':
                banquan = '无版权'

            env = Environment(loader=FileSystemLoader('./'))
            background_data = []
            button_background = []
            button_button = []
            button_info = []
            indorText = 'indor.txt'
            if os.path.exists(indorText):
                with open('indor.txt', 'r') as f:
                    button_info = json.loads(f.read())
            imgData = self.textEdit_2.toPlainText()
            if imgData != '':
                new_data = "".join((re.sub("\n", " ", imgData)).split(" "))
                str_to_dict = eval(new_data)
            if comboText == '下载按钮悬浮':
                if not tex:
                    QtWidgets.QMessageBox.about(self, '提示', "请先提交落地页数据")
                    return
                if str_to_dict['background'][0] == '图片地址':
                    return
                pop_bj = ''
                pop_down = ''
                if str_to_dict['popUp'] == '弹窗背景':
                    pop_bj = ''
                else:
                    pop_bj = str_to_dict['popUp']
                    pop_down = str_to_dict['popUpDown']
                video_img = '';
                video = ''
                video_icon = str_to_dict['video_icon'][0]
                if str_to_dict['video'][0] == '视屏地址':
                    video = '';
                else:
                    video = str_to_dict['video'][0]
                if str_to_dict['video_img'][0] == '视屏背景':
                    video_img = '';
                else:
                    video_img = str_to_dict['video_img'][0]
                for n in str_to_dict['background']:
                    background_data.append(n)

                template = env.get_template('./html/demo1.html')
                img1 = background_data
                with open(path_2020_html, 'w+', encoding="utf-8") as fout:
                    html_content = template.render(banquan=banquan, img1=img1, button_info=button_info,video_icon=video_icon,video=video,video_img = video_img,pop_bj=pop_bj,pop_down=pop_down,
                                                   buttonCss=buttonCss)
                    fout.write(html_content)
                # self.browser.setHtml('')
            elif comboText == '底部下载':
                if not tex:
                    QtWidgets.QMessageBox.about(self, '提示', "请先提交落地页数据")
                    return
                if str_to_dict['background'][0] == '图片地址':
                    return
                if str_to_dict['button_background'][0] == '按钮图片背景':
                    return
                if str_to_dict['button'][0] == '按钮图片按钮':
                    return
                pop_bj = ''
                pop_down = ''
                if str_to_dict['popUp'] == '弹窗背景':
                    pop_bj = ''
                else:
                    pop_bj = str_to_dict['popUp']
                    pop_down = str_to_dict['popUpDown']

                video_img = '';
                video = ''
                video_icon = str_to_dict['video_icon'][0]
                if str_to_dict['video'][0] == '视屏地址':
                    video = '';
                else:
                    video = str_to_dict['video'][0]
                if str_to_dict['video_img'][0] == '视屏背景':
                    video_img = '';
                else:
                    video_img = str_to_dict['video_img'][0]
                for n in str_to_dict['background']:
                    background_data.append(n)
                for k in str_to_dict['button_background']:
                    button_background.append(k)
                for j in str_to_dict['button']:
                    button_button.append(j)
                template = env.get_template('./html/demo2.html')
                img1 = background_data
                img2 = button_background
                img3 = button_button
                with open(path_2020_html, 'w+', encoding="utf-8") as fout:
                    html_content = template.render(banquan=banquan, img1=img1, img2=img2, img3=img3,video_icon=video_icon,video=video,video_img = video_img,
                                                   button_info=button_info,pop_bj=pop_bj,pop_down=pop_down)
                    fout.write(html_content)
            elif comboText == '不需要':
                template = env.get_template('./html/demo3.html')
                with open(path_2020_html, 'w+', encoding="utf-8") as fout:
                    html_content = template.render(banquan=banquan)
                    fout.write(html_content)
            elif comboText == '动态落地页模板':
                template = env.get_template('./html/demo4.html')
                with open(path_2020_html, 'w+', encoding="utf-8") as fout:
                    html_content = template.render(banquan=banquan)
                    fout.write(html_content)
            elif comboText == 'iframe':
                template = env.get_template('./html/demo5.html')
                iframeUrl = self.lineEdit_4.text()
                with open(path_2020_html, 'w+', encoding="utf-8") as fout:
                    html_content = template.render(banquan=banquan, iframeUrl=iframeUrl)
                    fout.write(html_content)
            elif comboText == '整屏幕横向轮播':
                if str_to_dict['background'][0] == '轮播图片':
                    return
                if str_to_dict['button_background'][0] == '按钮图片背景':
                    return
                if str_to_dict['button'][0] == '按钮图片按钮':
                    return
                for n in str_to_dict['background']:
                    background_data.append(n)
                for k in str_to_dict['button_background']:
                    button_background.append(k)
                for j in str_to_dict['button']:
                    button_button.append(j)
                template = env.get_template('./html/demo6.html')
                img1 = background_data
                img2 = button_background
                img3 = button_button
                with open(path_2020_html, 'w+', encoding="utf-8") as fout:
                    html_content = template.render(banquan=banquan, img1=img1, img2=img2, img3=img3)
                    fout.write(html_content)
            elif comboText == '底部下载，中间图片横向滑动':
                if not tex:
                    QtWidgets.QMessageBox.about(self, '提示', "请先提交落地页数据")
                    return
                background_top = [];
                background_slide = [];
                background_bottom = [];
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
                template = env.get_template('./html/demo7.html')
                img1 = background_data
                img2 = button_background
                img3 = button_button
                with open(path_2020_html, 'w+', encoding="utf-8") as fout:
                    html_content = template.render(banquan=banquan, background_top=background_top,
                                                   background_slide=background_slide,
                                                   background_bottom=background_bottom, img2=img2, img3=img3,
                                                   button_info=button_info)
                    fout.write(html_content)
            elif comboText == '底部下载，中间图片轮播':
                if not tex:
                    QtWidgets.QMessageBox.about(self, '提示', "请先提交落地页数据")
                    return
                background_top = [];
                background_slide = [];
                background_bottom = [];
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
                template = env.get_template('./html/demo8.html')
                img1 = background_data
                img2 = button_background
                img3 = button_button
                with open(path_2020_html, 'w+', encoding="utf-8") as fout:
                    html_content = template.render(banquan=banquan, background_top=background_top,
                                                   background_slide=background_slide,
                                                   background_bottom=background_bottom, img2=img2, img3=img3,
                                                   button_info=button_info)
                    fout.write(html_content)
            elif comboText == '全屏无缝滚动':
                if not tex:
                    QtWidgets.QMessageBox.about(self, '提示', "请先提交落地页数据")
                    return
                if str_to_dict['background_slide'][0] == '轮播图片':
                    return
                background = '';
                if str_to_dict['background'] == '背景图片':
                    background = ''
                else:
                    backround = str_to_dict['background']
                background_data = str_to_dict['background_slide'][0]

                template = env.get_template('./html/demo9.html')
                img1 = background_data

                with open(path_2020_html, 'w+', encoding="utf-8") as fout:
                    html_content = template.render(banquan=banquan, img1=img1, button_info=button_info,backround=backround,
                                                   buttonCss=buttonCss)
                    fout.write(html_content)
            QtWidgets.QMessageBox.about(self, '提示', "创建成功")
            indorText = 'indor.txt'
            if os.path.exists(indorText):
                os.remove(indorText)
        else:
            QtWidgets.QMessageBox.about(self, '提示', "文件已存在")
#--复制线上链接，生成html
    def getCopyHtml(self):
        url_ = self.lineEdit_7.text()
        hrml_path =  self.lineEdit_8.text()
        if hrml_path == '':
            return
        url = self.lineEdit.text()
        path_2020_html = "%s%s%s%s%s%s" % (lp_2020_path, '\\', url, '\\', hrml_path, '.html')
        is_true = os.access(path_2020_html, os.F_OK)
        if is_true:
            QtWidgets.QMessageBox.about(self, '提示', "文件已存在")
        else:
            req = requests.get(url=url_)
            html = req.text
            env = Environment(loader=FileSystemLoader('./'))
            template = env.get_template('./muban/lp5.html')
            with open(path_2020_html, 'w+', encoding="utf-8") as fout:
                html_content = template.render(html=html)
                fout.write(html_content)
            QtWidgets.QMessageBox.about(self, '提示', "创建成功")

