# for 迴圈
# 可用文字 /陣列
for x in "Hello":
    print(x)
for y in ["Hello", "world"]:
    print(y)

# range(數字) 從0開始 到數字-1(不包含該數字)
for x in range(11):
    print(x)
# range(數字1,數字2) 數字起始 到數字2前一個(不包含2)
for x in range(5, 10):
    print(x)
# 累加
sum = 0
for x in range(11):
    sum += x
print(sum)
