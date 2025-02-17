# Python 溫度轉換器

unit = input("請數入當前的溫度單位(攝氏C,華氏F)").upper()
temp = float(input("現在溫度:"))

if unit == 'C':
    temp = round((9 * temp / 5) + 32)
    print(f"當前溫度為 {temp} 度 F")
elif unit == 'F':
    temp = round((temp - 32) * 5 / 9)
    print(f"當前溫度為 {temp} 度 C")
else:
    print("溫度單位不正確")
