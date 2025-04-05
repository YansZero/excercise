# Python call back 回呼函式

# def test(*arg):
#     arg[0](arg[1]) #呼叫回呼函式
def test(arg, arg2):
    arg(arg2)  # 呼叫回呼函式


def handle(data):
    print(data)


# 將函式傳入另外一個另外一個函數當作參數
# 但test中參數會執行函式,變成回呼函式
test(handle, 50)


def add(n1, n2, cb):
    cb(n1 + n2)  # 使用回呼函式來顯示結果


def handle1(result):
    print("結果是", result)

def handle2(result):
    print("result is", result)


add(3, 4, handle1)
add(5, 6, handle2)
