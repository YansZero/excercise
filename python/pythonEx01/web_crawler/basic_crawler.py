import urllib.request as req
import bs4

# ★★★★★★★★★★重點★★★★★★★★★★
# 使用的是macOS系統：
# 首先要跑網頁使用url，需要多下
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# ★★★★★★★★★★重點★★★★★★★★★★

ptt_movie_url = "https://www.ptt.cc/bbs/movie/index.html"
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
request = req.Request(ptt_movie_url, headers={
    "User-agent": userAgent
})
# 先使用url簡易抓取,發現會出現urllib.error.HTTPError: HTTP Error 403: Forbidden
# with req.urlopen(ptt_movie_url) as res:
#     data = res.read().decode("utf-8")
#     print(data)

# 要看似正常的使用者 模擬操作, 要使用request去請求
with req.urlopen(request) as res:
    data = res.read().decode("utf-8")
# print(data)

# 讓BeautifulSoup 找到我們想要的部分
root = bs4.BeautifulSoup(data, "html.parser")
# print(root)
# print(root.title.string)
# 尋找class="title" 的div
# 只找特定的 find
title_simple = root.find("div", class_="title")
# 找所有符合的元素 find_all,會是一個list
titles = root.find_all("div", class_="title")
print(titles)

for title in titles:
    if title.a == None:  # 如果標題包含a標籤(沒有被刪除的話)
        print("空標題")
    else:
        print(f"標題是:{title.a.string}")
