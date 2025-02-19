# Python for 迴圈

# in 後面接可迭代的
# range(start,end) 但不包含end
for x in range(1, 11):
    print(x)
# reversed 相反
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
