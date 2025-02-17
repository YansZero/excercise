# 利用PYTHON 做出二分法
# 需在有序的數列中 找到資料

arrList = [-32, -8, -4, -1, 1, 4, 7, 10, 20, 33]
print("陣列如下:", arrList)
mTarget = int(input("二分法測試，請輸入要找尋的數字:"))

headNum = 0
endNum = len(arrList) - 1
middle = 0
mcheck = False

while (headNum < endNum):
    middle = int((endNum + headNum) / 2)
    if (mTarget == arrList[middle]):
        print("找到目標數字位置在", middle)
        mcheck = True
        break
    else:
        # 需要防呆 若介於兩個陣列數字中卻一直找不到，就得跳出去，避免無限迴圈
        if ((headNum + 1) == endNum) and ((mTarget > arrList[headNum]) and ((mtarget < arrList[endNum]))):
            break
        elif mTarget < arrList[middle]:
            endNum = middle
        else:
            headNum = middle

if not mcheck:
    print("陣列中找不到該數字!")
