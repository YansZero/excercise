# Python中的Lambda λ

# Lambda 有函式的功能 一行就可以寫完
# 可傳參數

# example: double
# def double_fun(x):
#     return x * 2
#
# print(double_fun(10))
# double2 = lambda x: x * 2
# print(double2(50))

# example2 傳兩個參數
# multiple = lambda x, y: x * y
# print(multiple(2, 3))

# example3 if else條件語句
# result = lambda x: f"{x}是偶數" if x % 2 == 0 else f"{x}是奇數"
# print(result(87))
# print(result(56))

# example4 處理字串
full_name = lambda first_name, last_name: f"{first_name}{last_name}"

print(full_name("悟空","孫"))
