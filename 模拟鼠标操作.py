from selenium import webdriver
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver import ActionChains
#创建浏览器对象


def main():
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    # 打印页面标题“百度一下你就知道”
    # 鼠标移动到某处
    action1 = driver.find_element_by_id("su")
    ActionChains(driver).move_to_element(action1).perform()
    # 鼠标移动到某处单击
    action2 = driver.find_element_by_id("su")
    ActionChains(driver).move_to_element(action2).click(action2).perform()  # 鼠标移动到某处双击
    action3 = driver.find_element_by_id("su")
    ActionChains(driver).move_to_element(action3).double_click(action3).perform()  # 鼠标移动到某处右击
    action4 = driver.find_element_by_id("su")
    ActionChains(driver).move_to_element(action4).context_click(action4).perform()
    print(driver.title)
if __name__ == '__main__':
    main()