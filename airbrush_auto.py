# 导模块
import time
from selenium.webdriver.common.by import By

from appium import webdriver
# 创建一个字典，包装相应的启动参数
desired_caps = dict()
# 需要连接的手机的平台(不限制大小写)
desired_caps['platformName'] = 'Android'
# 需要连接的手机的版本号(比如 5.2.1 的版本可以填写 5.2.1 或 5.2 或 5 ，以此类推)
desired_caps['platformVersion'] = '7.1.2'
# 需要连接的手机的设备号(andoird平台下，可以随便写，但是不能不写)
desired_caps['deviceName'] = '1'
# desired_caps['deviceName'] = 'c854e0da7d63    device'
# 需要启动的程序的包名
desired_caps['appPackage'] = 'com.magicv.airbrush'
# 需要启动的程序的界面名
desired_caps['appActivity'] = '.Settings'
# 连接appium服务器
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

search_button=driver.find_element(By.ID,"com.magicv.airbrush:id/tv_skip")

# driver.find_element(By.CLASS_NAME,"android.widget.TextView").click()

# driver.find_element(By.ID,"android:id/search_src_text").send_keys("蓝牙")
time.sleep(5)
driver.find_element(By.XPATH,"//*[@content-desc='收起']").click()

time.sleep(3)
# 退出
driver.quit()
