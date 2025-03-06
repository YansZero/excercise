# Python 購物車程式

# list , set, tuple

goodsList = []
priceList = []

# 無窮迴圈
while True:
    good = input("請輸入想買的商品:")
    if good.lower() == "q":
        break
    price = float(input(f"請輸入{good}的價格:"))
    goodsList.append(good)
    priceList.append(price)

# print("商品有:", goodsList)
# print("價格為:", priceList)
# 列出明細
for index, good in enumerate(goodsList):
    print(f"第{index + 1}個商品是{good},價格為{priceList[index]:.2f}")

# 總價格
total = sum(priceList)
print(f"全部購買金額為{total:.2f}")
