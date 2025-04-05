# Python for 迴圈

# in 後面接可迭代的
# range(start,end) 但不包含end
print(f"使用range三個參數 range(1, 11),結果為1...10")
for x in range(1, 11):
    print(x)
# range(start,end,step) 但不包含end,每次以step作推進
print(f"使用range三個參數 range(1, 11, 3),結果為1,4,7,10")
for z in range(1, 11, 3):
    print(z)

# reversed 相反
print(f"使用reversed完成倒數reversed(range(1, 11),結果為10..1")
for y in reversed(range(1, 11)):
    print(y)
print("Happy New Year!")

# 字串可以迭代
credit_card = "2325-6578-8521-9584"
# for no in credit_card:
#     print(no)

# continue
for no in credit_card:
    if no == "8":
        # continue #非8的繼續執行
        break  # 到8就結束執行
    print(no)

# 字典也可以迭代
# 如果使用for x in my_dict 只會列印key值
# 若都要使用字典.items()
my_dict = {"a": 1, "b": 2, "c": 3}
for key, value in my_dict.items():
    print("my_dict:", key, ",", value)
