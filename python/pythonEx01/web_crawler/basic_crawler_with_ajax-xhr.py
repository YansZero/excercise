# Python 爬蟲搭配 AJAX / XHR  技術
# AJAX 前端js的技術 (發送第二次請求到網頁,取得資料並產生HTML網頁)
# 流程如下:
# ------------      發送請求到xyz.com      --------------
# ' xyz.com  '       --------------->     '           '
# '          '      取得不帶資料的HTML網頁   '           '
# '          '      <----------------     '           '
# '   瀏覽器  '      發送第二次請求到xyz.com  ' 網站伺服器  '
# '   Chrome '      ---------------->     ' Web Server'
# '          '     取得資料並產生HTML網頁    '           '
# '          '      <----------------     '           '
# ------------                            ------------
#練習抓取 PCHome 限時特賣的產品
import urllib.request as request
import json

on_sale_url = "https://ecapi-cdn.pchome.com.tw/fsapi/cms/onsale"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
req = request.Request(on_sale_url, headers={
    "User-agent": user_agent
})

with request.urlopen(req) as response: #根據觀察回來的是json格式
    #sales_data=response.read().decode("utf-8")
    sales_data = json.load(response)

# print(sales_data)
sales_item_list = sales_data["data"]

for sales_item in sales_item_list:
    print(f"特賣開始時間{sales_item['startTime']},結束時間{sales_item['endTime']}")
    print("-----------特賣產品清單-------------------")
    for product in sales_item['products']:
        print(f"產品名稱:{product['name']},原價:{product['price']['origin']},特價:{product['price']['onsale']}")
    print("----------------------------------------")