
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject, pyqtSlot, QUrl
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys


class Print(QObject):
    # pyqtSlot，中文网络上大多称其为槽。作用是接收网页发起的信号
    @pyqtSlot(str, result=str)
    def print(self, content):
        print('输出文本：' ,content)  # 对接收到的内容进行处理，比如调用打印机进行打印等等。此处略去，只在bash中显示接收到的消息
        return content


if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = QWebEngineView()  # 新增一个浏览器引擎
    browser.setWindowTitle('QWebChannel交互Demo')
    browser.resize(900, 600)
    channel = QWebChannel()  # 增加一个通信中需要用到的频道
    printer = Print()  # 通信过程中需要使用到的功能类
    channel.registerObject('printer', printer)  # 将功能类注册到频道中，注册名可以任意，但将在网页中作为标识
    browser.page().setWebChannel(channel)  # 在浏览器中设置该频道
    url_string = "file:///C:/Users/Administrator/Desktop/python/可视化窗口pyqt5/前后交互/demo.html"  # 内置的网页地址，此处我采用的是本地的。远程同样可以使用。
    browser.load(QUrl(url_string))
    browser.show()
    sys.exit(app.exec_())
