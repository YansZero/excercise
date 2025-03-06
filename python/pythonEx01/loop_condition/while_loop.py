# Python While迴圈

# name = input("請數入你的名字:")
# if name=="":
#     print("你沒有輸入名字!")
# else:
#     print("您好",name)

# 範例1
# 用While迴圈來執行
# name = ""
# while name == "":
#     name = input("請數入你的名字:")
# print("您好", name)

# 範例2
# food = input("請輸入你喜歡吃的食物:")
# while food != "q":
#     print(f"你喜歡的食物是{food}")
#     food = input("請輸入你喜歡吃的食物:")
# print("再見")

# 範例3
num = int(input("請輸入1~10的整數:"))

while not num in range(1,11):
    print("輸入非1~10整數")
    num = int(input("請輸入1~10的整數:"))
print(f"你輸入的數字為: {num}")