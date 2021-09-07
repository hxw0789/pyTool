import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()  # 窗口最大化
driver.implicitly_wait(30)
driver.get("https://pre-negotiate.jiarong.cn/login.html")  # 打开浏览器
time.sleep(1)
driver.find_element_by_name("account").send_keys("144815")
driver.find_element_by_name("password").send_keys("123456")
time.sleep(1)
driver.find_element_by_xpath("//*[text()='登录']").click()
time.sleep(6)
driver.quit()
