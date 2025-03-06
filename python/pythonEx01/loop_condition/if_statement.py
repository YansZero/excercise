# if-else 控制流程

# Boolean 布林值
for_sale = True
if for_sale:
    print("東西販賣中")
else:
    print("東西未販售")

age = int(input("請輸入你的年齡:"))
if age >= 100:
    print("太老了~無法註冊")
elif age >= 18:
    print("合法可以註冊")
elif 0 <= age < 18:
    print("你要年滿18才能註冊")
else:
    print("年齡錯誤~不可以註冊")
