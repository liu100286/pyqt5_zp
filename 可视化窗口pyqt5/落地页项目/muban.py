class get_muban(object):
    #   下拉
    def muban_info(self, text):
        self.iframe = False
        self.comboText = text;
        if text == '下载按钮悬浮':
            self.textEdit_2.setVisible(True)
            self.textEdit_2.setPlainText("""{
"background":[
"图片地址",
],
"xuanfu":[
"按钮悬浮图片地址"
],
"no_xuanfu":[
"按钮不悬浮图片地址"
],
'video_img':[
"视屏背景"
],
'video_icon':[
'http://img.zntec.mobi/0.42546545550013803.png'
],
'video':[
"视屏地址"
],
'popUp':'弹窗背景',
'popUpDown':'弹窗背景下载',
'zhezhao_pop':0,
'zhezhao_down':0,
}""")
        elif text == '底部下载':
            self.textEdit_2.setPlainText("""{
"background":[
"图片地址",
],
"button_background":[
"按钮图片背景"
],
"button":[
"按钮图片按钮"
],
"no_xuanfu":[
"按钮不悬浮图片地址"
],
'video_img':[
"视屏背景"
],
'video_icon':[
'http://img.zntec.mobi/0.42546545550013803.png'
],
'video':[
"视屏地址"
],
'popUp':'弹窗背景',
'popUpDown':'弹窗背景下载',
'zhezhao_pop':0,
'zhezhao_down':0,
}""")
        elif text == '不需要':
            self.textEdit_2.setPlainText('')
        elif text == '动态落地页模板':
            self.textEdit_2.setPlainText('')
        elif text == 'iframe':
            self.textEdit_2.setPlainText('')
            self.iframe = True
        elif text == '整屏幕横向轮播':
            self.textEdit_2.setPlainText("""{
"background":[
"轮播图片",
],
"button_background":[
"按钮图片背景"
],
"button":[
"按钮图片按钮"
]
}""")
        elif text == '底部下载，中间图片横向滑动':
            self.textEdit_2.setPlainText("""{
"background_top":[
"顶部图片地址",
],
"background_slide":[
"滑动图片地址",
],
"background_bottom":[
"底部图片地址",
],
"button_background":[
"按钮图片背景"
],
"button":[
"按钮图片按钮"
],
"no_xuanfu":[
"按钮不悬浮图片地址"
],
'zhezhao':0,
}""")
        elif text == '底部下载，中间图片轮播':
            self.textEdit_2.setPlainText("""{
"background_top":[
"顶部图片地址",
],
"background_slide":[
"轮播图片地址",
],
"background_bottom":[
"底部图片地址",
],
"button_background":[
"按钮图片背景"
],
"button":[
"按钮图片按钮"
],
"no_xuanfu":[
"按钮不悬浮图片地址"
],
'zhezhao':0,
}""")
        elif text == '全屏无缝滚动':
            self.textEdit_2.setPlainText("""{
"background_slide":[
"轮播图片",
],
'background':'背景图片',
"down_img":[
"下载按钮图片",
],
"xuanfu":[
"悬浮图片"
],
}""")
        self.iframe_info(self)
    # ----------------------------------判断文件夹是否存在，创建文件夹