# Python 將函式指派給變數

def hello():
    print("您好")


hi = hello
# 這時候因為沒有括號,所以不會執行hello內的程式
# 讓變數加上()就會開始執行
hi()
# 把hello跟hi印出來,會發現他們的記憶體一樣
print(hello)
print(hi)
