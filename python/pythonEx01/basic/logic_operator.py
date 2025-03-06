# Python 中的邏輯運算子

# and or not

temp = int(input("請輸入當前溫度: "))

if 18 <= temp <= 28:
    print(f"當前溫度{temp}很舒適")
elif temp >=29 and temp <40:
    print(f"當前溫度{temp}很熱")
elif 10 <= temp <18:
    print(f"當前溫度{temp}有點冷")
elif 10 < temp or temp >= 40 :
    print(f"當前溫度{temp}有狀況,快躲起來")
else:
    print(f"當前溫度{temp}有異常")
    exit()
