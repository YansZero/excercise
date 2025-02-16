import math

# Python 數學
# 加減乘除

# + / -
apples = 3
print(apples)
apples = apples + 1
print(apples)
apples += 1
print(apples)
apples = apples - 1
print(apples)
apples -= 1
print(apples)

# * 或者 /
apples = apples * 2
print(apples)
apples *= 2
print(apples)

apples = apples / 2
print(apples)
apples /= 2
print(apples)

# 指數 三次方
apples = 3
print(apples)
# apples = apples **2
apples **= 2
print(apples)

# mod 取餘數
# 10 mod 3 = 1
# 11 mod 3 = 2
# 12 mod 3 = 0
print(f"取餘數: 10%3= {10 % 3}")
print(f"取餘數: 11%3= {11 % 3}")
print(f"取餘數: 12%3= {12 % 3}")

# 次方 pow
print(f"3的2次方={pow(3, 2)}")

# max(m1,m2,...) / min(n1,n2,...)
print(f"3,4,5取最大值:{max(3, 4, 5)}")
print(f"99,33,88取最小值:{min(99, 33, 88)}")

# 絕對值
c = -4
print(f"c原本的值{c},絕對值後:{abs(c)}")

# 四捨五入 round(參數,精度)
print(f"3.14四捨五入:{round(3.14)}")
print(f"3.5四捨五入:{round(3.5)}")
print(f"3.78642四捨五入:{round(3.78642, 2)}")

# 無條件進位、無條件捨去
d = 9.5
print(f"無條件進位math.ceil: {math.ceil(d)}")
print(f"無條件捨去math.floor: {math.floor(d)}")

# 圓周率π
print(f"圓周率π={math.pi}")

# 計算圓的周長 2πr
radius = float(input("請數入圓的半徑"))
circle_length = 2 * math.pi * radius
print(f"圓的周長 2πr={ round(circle_length,2)}")

# 計算圓的面積 πr*2
res = math.pi * pow(radius,2)
print(f"圓的面積 π*pow(radius,2),={ round(res,2)}")

res2 = math.pi * radius**2
print(f"圓的面積使用 π*radius**2 ={ round(res2,2)}")