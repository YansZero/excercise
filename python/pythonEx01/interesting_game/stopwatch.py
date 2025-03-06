import time

#倒數 time.sleep(1)

my_time = int(input("請輸入秒數:"))
# range(num,num2,num3) num3 = -1 是倒著數
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = x // 60 % 60 # /:會顯示浮點數 //:顯示整數
    print(f"{minutes:02}:{seconds:02}")
    time.sleep(1)
print("時間到了")
