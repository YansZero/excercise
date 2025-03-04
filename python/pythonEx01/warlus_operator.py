# Python 3.8之後 獠牙運算符 :=

# 用來簡潔程式碼
# 獠牙運算符
# 賦值表達式 :=
# 賦值運算子 =

happy = True
print(happy)
print(happy := False)

# 簡化前
# foods = []
# while True:
#     food = input("你喜歡什麼食物:")
#     if food=='quit':
#         break
#     foods.append(food)
#
# print(foods)

# 簡化 第一次
# foods = []
# while food := input("你喜歡什麼食物:"):
#     if food=='quit':
#         break
#     foods.append(food)
#
# print(foods)

foods = []
while (food := input("你喜歡什麼食物:")) !='quit':
    # if food=='quit':
    #     break
    foods.append(food)

print(foods)