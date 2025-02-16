# input 取得使用者輸入
# 基本輸入 用字串儲存
name = input("請輸入名字:")
print(f"你的名字是: {name}")

# ex01: 填詞遊戲
adj01 = input("請輸入第1個形容詞:")
noun01 = input("請輸入第1個名詞:")
adj02 = input("請輸入第2個形容詞:")
verb01 = input("請輸入第1個動詞:")
adj03 = input("請輸入第3個形容詞:")
noun02 = input("請輸入第2個名詞:")

print(f"今天是一個{adj01}的天氣，外面的{noun01}很{adj02}，我{verb01}，換上{adj03}的{noun02}")

# ex02 計算矩形面積
length = float(input("請輸入矩形長度: "))
width = float(input("請輸入矩形寬度: "))

area = length * width

print(f"矩形面積area= {area} 平方公分")

# ex03 計算購物車程式

item = input("您想買什麼東西? ")
quantity = int(input("您想買幾個? "))
price = float(input("單價多少? "))

total = quantity * price

print(f"物品{item},總共{total}元")