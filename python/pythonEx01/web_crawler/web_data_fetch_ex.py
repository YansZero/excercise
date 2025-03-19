# 網路連線
import urllib.request as request
import ssl

# urlopen https時需要驗證一次SSL證書，當網站目標使用自簽名的證書時就會跳出這個錯誤。
# 所以這裡可以使用SSL module把證書驗證改成不需要驗證即可
ssl._create_default_https_context = ssl._create_unverified_context

urlSource = "https://www.ntu.edu.tw"
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"

req = request.Request(urlSource, headers={
    "User-agent": userAgent
})
# 串接 擷取公開資料
# with request.urlopen(urlSource) as response:
#     data = response.read().decode("utf-8")
# print("urlopen使用url方式打開的網頁:", data)

# 或者使用 request方式開啟
# with request.urlopen(req) as response:
#     data2 = response.read().decode("utf-8")
# print("urlopen使用request方式打開的網頁:", data2)

import json
openDataUrl = '	https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire'

with request.urlopen(openDataUrl) as response:
    data = json.load(response) # 利用json處理json格式

print(data)

#取得公司名稱
companyList = data['result']['results']
print(f"companyList:{companyList}")
with open("company.txt",'w',encoding='utf-8') as file:
    for company in companyList:
        file.write(company['公司名稱'] + '\n')
        print(company['公司名稱'])

