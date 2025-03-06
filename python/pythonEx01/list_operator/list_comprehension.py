# Python中的列表推導式(list comprehension)
# 列表推導式 =>更少的語法創建新列表
# [表達式 for 變數 in 可迭代對象 if 條件]
# 適用場景:產生清單，如篩選數字、變換字串等
# 比lambda好懂
# 平方

def square(x):
    return x * x


listTemp = []
for i in range(1, 11):
    listTemp.append(square(i))
print(f"一般方式:{listTemp}")

tempList = [i ** 2 for i in range(1, 11)]
print(f"列表推導式:{tempList}")

grades = [100, 90, 66, 80, 52, 77, 30, 15, 29]
pass_grade = [grade for grade in grades if grade >= 60]
print(pass_grade)
