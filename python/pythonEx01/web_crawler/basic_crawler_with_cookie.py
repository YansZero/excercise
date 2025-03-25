import urllib.request as req
import bs4


# ★★★★★★★★★★重點★★★★★★★★★★
# 首先要跑網頁使用url，需要多下
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# ★★★★★★★★★★重點★★★★★★★★★★
# Python 爬蟲搭配Cookies

def get_page_data(url):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    cookies = "over18=1"  # 搭配cookie使用
    request = req.Request(url, headers={
        "User-agent": user_agent,
        "Cookie": cookies
    })

    # 要看似正常的使用者 模擬操作, 要使用request去請求
    with req.urlopen(request) as res:
        data = res.read().decode("utf-8")

    # 讓BeautifulSoup 找到我們想要的部分
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")
    for title in titles:
        if title.a is None:  # 如果標題包含a標籤(沒有被刪除的話)
            print("空標題")
        else:
            print(f"標題是:{title.a.string}")
    # 要抓上一頁的連結
    # 只找特定的 find,使用string="要尋找元素內的內容"
    page_previous = root.find("a", string="‹ 上頁")
    return page_previous["href"]


#
baseUrl = "https://www.ptt.cc"
#ptt_gossip_url = baseUrl + "/bbs/gossiping/index.html"
page_url= baseUrl + "/bbs/gossiping/index.html"
# 一次抓10葉
for i in range(10):
    print(f"★★★★★★★★★★當前網址為{page_url} 開始★★★★★★★★★★")
    next_link = baseUrl + get_page_data(page_url)
    print(f"★★★★★★★★★★當前網址為{page_url} 結束★★★★★★★★★★")
    page_url = next_link
    print(f"預計新網址為{page_url}")
