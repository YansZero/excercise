# 複利計算機
# 總金額 = 本金 * (1+(利率/100)) ** 時間

# 10000 * 1.05 * 1.05
# 10000 * (1 + (5/100)) ** 2

# amount = 0
# while amount <= 0:
#     amount = float(input("請輸入本金金額:"))
#     if amount <= 0:
#         print("本金不可小於或者等於零")
# print("你的本金為:",amount)


# rate = 0
# while rate <=0 :
#     rate = float(input("請輸入利率:"))
#     if rate <= 0:
#         print("利率不可小於或者等於零")
# print("你的利率為:",rate)

# time = 0
# while time <=0:
#     time = int(input("請輸入年限:"))
#     if time<=0:
#         print("年限不可小於或者等於零")
# print("你的年限為:",time)

amount = 0
rate = 0
time = 0

while amount <= 0:
    amount = float(input("請輸入本金金額:"))
    if amount <= 0:
        print("本金不可小於或者等於零")

while rate <= 0:
    rate = float(input("請輸入利率:"))
    if rate <= 0:
        print("利率不可小於或者等於零")

while time <= 0:
    time = int(input("請輸入年限:"))
    if time <= 0:
        print("年限不可小於或者等於零")

print("你的本金為:", amount)
print("你的利率為:", rate)
print("你的年限為:", time)

totalMoney = amount * (1 + (rate / 100)) ** time

print("你最終獲利金額為:", totalMoney)
