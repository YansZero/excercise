# Python中 sort方法

# sort

# list
# 數字
print("-----------數字排序 BEGIN----------------")
num_list = [1, 5, 9, 8, 4, 2]
print(num_list)
# 使用sort排序
num_list.sort()
print(num_list)
# sort(reverse=True) 跟 reverse()效果一樣擇一即可
# 如果連續使用則會再倒序一次
num_list.sort(reverse=True)
print(num_list)
num_list.reverse()
print(num_list)
print("-----------數字排序 END----------------")

# string排序則用第一字元開始比較,有相同才往後的字元比較
print("-----------字串排序 BEGIN----------------")
str_list = ['Jack', 'Andy', 'Tom', 'Lin', 'Jason']
print(str_list)
str_list.sort()
print(str_list)
str_list.sort(reverse=True)
print(str_list)
print("-----------字串排序 END----------------")

# 元組 Tuple排列,使用sorted
students = [
    ("小明", 170, "A"), ("小華", 169, "C"), ("老王", 180, "B")
]
print("-----------元組Tuple排序 BEGIN----------------")
print(f"學生資料:{students}")
name_sorted_student = sorted(students, key=lambda student: student[0])
height_sorted_student = sorted(students, key=lambda student: student[1], reverse=True)
score_sorted_student = sorted(students, key=lambda student: student[2])
print(f"學生依照名字排序:{name_sorted_student}")
print(f"學生依照身高排序(高->矮):{height_sorted_student}")
print(f"學生依照分數排序:{score_sorted_student}")
print("-----------元組Tuple排序 END----------------")
