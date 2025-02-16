import urllib.request as request  #網路連線模組
import json 

src=" https://datacenter.taichung.gov.tw/swagger/OpenData/678b53a2-6de4-4052-90b4-0847eb1d7a5b"
with request.urlopen(src) as response:
    # data=response.read().decode("utf-8") #先判斷是否是JSON檔案
    data = json.load(response) #利用JSON模組處理JSON資料格式

print(data)    

with open("hotel.txt",mode="w",encoding="utf-8") as file:
    file.write("經營名稱" + "\t" + "標章到期日" +"\n")
    for item in data :
        file.write(item["經營名稱"]+"\t"+ item["標章到期日"] +"\n")


    