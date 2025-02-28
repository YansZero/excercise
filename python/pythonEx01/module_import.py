# python 中的模組 module
# 使用 import 模組名稱 import math
# 可以使用別名 as 別名名稱
# 可以單獨引入子模組 from 模組 import子模組
# import math as m
#
# print(m.pi)
# print(m.pow(3, 2))
#
# number = 20.65423
# print(m.ceil(number))
# print(m.floor(number))
# print(round(number, 3))

# 練習使用自己寫的模組
import my_module as m
print(m.pi)
print(m.square(3))
print(m.cube(3))
print(m.area(6))