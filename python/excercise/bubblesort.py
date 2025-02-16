# 冒泡排序法
# 比較相鄰兩個數字
# 將陣列中順序自由下排到大

arrList=[49,38,65,97,76,13,27,49]
print("arrList-Before:",arrList)


arrList.sort()
print("USE list.sort arrList-After :",arrList)

for x in range(len(arrList)-1):
    temp = arrList[x]
    if (arrList[x] > arrList[x+1]):
        arrList[x]  = arrList[x+1]
        arrList[x+1]= arrList[x]

print("USE for loop arrList-After :",arrList)        