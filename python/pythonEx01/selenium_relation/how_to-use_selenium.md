# Python Selenium 網頁爬蟲基礎
參考網站https://selenium-python.readthedocs.io/locating-elements.html

---
# 基本語法
```
# 載入selenium 相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 設定chrome driver的執行檔路徑
chrome_driver_path = r"{path}\chromedriver.exe"
options = Options()
options.chrome_executable_path = chrome_driver_path

# 建立driver物件實體,用程式操作瀏覽器運作

driver = webdriver.Chrome(options=options)
driver.maximize_window()  # 視窗最大化
driver.get(url)  # 連線到特定網頁
driver.save_screenshot(file name)  # 螢幕截圖 並存成特定圖片名稱
driver.close() #關閉瀏覽器
```
### ★★★★★Driver 搜尋方法 start★★★★★
### 取得滿足條件的一個標籤的WebElement(通用規則)
```
driver.find_element(搜尋欄位,搜尋條件)
```
### 取得滿足條件的所有標籤的WebElement List
```
driver.find_elements(搜尋欄位,搜尋條件)
```
---

詳細用法
---
### 根據連結標籤的文字搜尋
```
driver.find_element(By.LINK_TEXT,搜尋條件)
driver.find_elements(By.LINK_TEXT,搜尋條件)
```
---
### 連結標籤內部分文字搜尋
```
driver.find_element(By.PARTIAL_LINK_TEXT, 'Conti')
driver.find_elements(By.PARTIAL_LINK_TEXT, 'Conti')
```
---
### 找尋標籤內 name的名稱
```
<html>
  <body>
   <form id="loginForm">
    <input name="username" type="text" />
    <input name="password" type="password" />
    <input name="continue" type="submit" value="Login" />
    <input name="continue" type="button" value="Clear" />
   </form>
 </body>
</html>
```
```
username = driver.find_element(By.NAME, 'username')
username = driver.find_elements(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
password = driver.find_elements(By.NAME, 'password')
```
---
### 找尋元素標籤 依據Tag 名稱
```
 <html>
  <body>
   <h1>Welcome</h1>
   <p>Site content goes here.</p>
 </body>
 </html>

heading1 = driver.find_element(By.TAG_NAME, 'h1')
```
---
```
<html>
 <body>
  <p class="content">Site content goes here.</p>
 </body>
</html>
```
### 找尋元素標籤 依據CSS 名稱
```
content = driver.find_element(By.CLASS_NAME, 'content')
content = driver.find_elements(By.CLASS_NAME, 'content')
```
### 找尋元素標籤 CSS 選擇器
```
content = driver.find_element(By.CSS_SELECTOR, 'p.content')
content = driver.find_elements(By.CSS_SELECTOR, 'p.content')
```
---
### ★★★★★Driver 搜尋方法 end★★★★★

---
### 對元素的操作
```
element = driver.find_element(搜尋欄位,搜尋條件)
```
---
### # 取得標籤得文字
```
element.text
```
---
### 取得某個屬性
```
element.get_attribute("屬性名稱")
```
---
### 模擬使用者觸發事件
### 模擬使用者點擊
```
element.click()
```
---