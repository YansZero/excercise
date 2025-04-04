# Python Selenium 快速開始、網頁截圖
# 載入selenium 相關模組
# 基本語法
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# chrome_driver_path = r"E:\coding\excercise\chromedriver-win64\chromedriver.exe"
# # 設定chrome driver的執行檔路徑
# options = Options()
# options.chrome_executable_path = chrome_driver_path
#
# # 建立driver物件實體,用程式操作瀏覽器運作
# # driver = webdriver.Chrome(options=options)
# driver =webdriver.Chrome()
# driver.maximize_window()  # 視窗最大化
# driver.get(url)  # 連線到特定網頁
# driver.save_screenshot(file name)  # 螢幕截圖 並存成特定圖片名稱
# driver.close() #關閉瀏覽器

# 由chatgpt 建議
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_driver_path = r"E:\coding\excercise\chromedriver-win64\chromedriver.exe"

# 設定 Chrome Options
options = Options()
service = Service(chrome_driver_path)  # 設定 driver 服務

# 建立 driver 物件
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()  # 視窗最大化

# 開啟 Google 並截圖
driver.get("https://www.google.com")
driver.save_screenshot("screenshot-google.png")

# 開啟 Yahoo 並截圖
driver.get("https://tw.yahoo.com")
driver.save_screenshot("screenshot-yahoo.png")

# **改用 quit() 正確關閉瀏覽器**
driver.quit()
