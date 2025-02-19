# 巢狀迴圈
# for x in range(1, 10):
#     print(x, end=" ")
#
# for y in range(5):
#     for x in range(1, 10):
#         print(x, end=" ")
#     print()

row = int(input("請輸入列數:"))
cols = int(input("請輸入行數:"))
symbol = input("請輸入符號:")

for i in range(row):
    for j in range(cols):
        print(symbol, end=" ")
    print("\n")
