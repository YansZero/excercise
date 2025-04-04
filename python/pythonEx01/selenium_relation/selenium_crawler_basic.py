# Python Selenium 網頁爬蟲基礎
# 參考網站https://selenium-python.readthedocs.io/locating-elements.html

## ★★★★★Driver 搜尋方法 start★★★★★
## 取得滿足條件的一個標籤的WebElement(通用規則)
# driver.find_element(搜尋欄位,搜尋條件)
## 取得滿足條件的所有標籤的WebElement List
# driver.find_elements(搜尋欄位,搜尋條件)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_driver_path = r"E:\coding\excercise\chromedriver-win64\chromedriver.exe"
# 設定chrome driver的執行檔路徑
options = Options()
options.chrome_executable_path = chrome_driver_path

# 建立driver物件實體,用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)
driver.maximize_window()  # 視窗最大化

searchTitleList = []


# 取得當前股票版頁面所有標題
def get_all_title_from_url(url):
    driver.get(url)
    title_list = driver.find_elements(By.CLASS_NAME, "title")  # 抓取所有 class="title"的元素
    for title in title_list:
        searchTitleList.append(title.text)


def get_all_title_from_page():
    title_list = driver.find_elements(By.CLASS_NAME, "title")  # 抓取所有 class="title"的元素
    for title in title_list:
        searchTitleList.append(title.text)


# 取得上一頁的元素,並回傳網址
def get_previous_page_link():
    previous_element = driver.find_element(By.LINK_TEXT, "‹ 上頁")
    return previous_element.get_attribute("href")


def click_previous_page_link():
    previous_element = driver.find_element(By.LINK_TEXT, "‹ 上頁")
    previous_element.click()


# 爬ptt股票版
baseUrl = "https://www.ptt.cc"
target_url = baseUrl + "/bbs/stock/index.html"
driver.get(target_url)  # 連線到特定網頁
# print(driver.page_source) #網頁原始碼
for i in range(10):
    # 方法一, 取得連結後再抓取title
    # get_all_title_from_url(target_url)
    # target_url = get_previous_page_link()
    # 方法二, 模擬使用者點擊上一頁後再抓取title
    get_all_title_from_page()
    click_previous_page_link()

for searchTitle in searchTitleList:
    print(searchTitle)

driver.quit()
