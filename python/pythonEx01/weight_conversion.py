# Python 體重轉換器

weight = float(input("請輸入你的體重:"))
unit = input("請輸入體重的單位公斤還是磅?(kg,lb)").upper()

if unit=='KG':
    weight *= 2.2
    newUnit = '磅'
elif unit=='LB':
    weight /= 2.2
    newUnit = '公斤'
else:
    print('單位不正確')
    exit()

print(f"你的體重是{weight,newUnit}")
