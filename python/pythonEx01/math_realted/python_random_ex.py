import random

# 查看方法
# help(random)

# randint(start,end)
# 回傳 int 介於start 以及end之間,包含start以及end
print(random.randint(1, 10))

# random()
# 回傳0~1之間的浮點數
# print(random.random())
# 列表中隨機一個元素 choice
options = ["剪刀", "石頭", "布"]
print("options的選項", options)
rand_option = random.choice(options)
print(f"random.choice後電腦隨機選擇是:{rand_option}")

# sample,在list中隨機取出num個數
# random.sample(list,num)
tempList = [1,5,6,12,19,20]
print(f"tempList:{tempList}")
print(f"random.sample後結果{random.sample(tempList,4)}")

# uniform(start,end) start~end之間機率相同
print(random.uniform(0.0, 1.0))
# normalvariate(num,num2) 取得平均數num, 標準差10的
# 常態分配亂數(大部分取到的數字會落在 num +- num2)
num = 100
num2= 10
print(f"常態分配亂數,基準值{num},標準差{num2}")
for i in range(1,11):
    test = random.normalvariate(num, num2)
    print(f"常態分配亂數第{i}的值{test}")

# 將一個列表就地打亂
cards = ["2", "3", "4", "5", "6", "7", "8", "9"]
print(f"card原本{cards}")
random.shuffle(cards)
print(f"card打亂後{cards}")

# guess number
low = 1
high = 100
final_number = random.randint(low, high)
guessTime = 0

print(f"猜數字遊戲即將開始,你將輸入{low}~{high}的任一數字,系統會隨機設置{low}~{high}其中一個數字")
while True:
    guess_number = int(input(f"請輸數{low}~{high}數字:"))
    guessTime += 1
    if guess_number > final_number:
        print("你的數字太大了,加油再試看看!")
    elif guess_number < final_number:
        print("你的數字太小了,加油再試看看!")
    else:
        print(f"恭喜你猜對了! 系統數字為{guess_number},總共猜了{guessTime}次")
        break
