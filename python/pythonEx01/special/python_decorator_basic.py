# Python 裝飾器 Decorator
# 特殊設計的函式
# 用來[輔助]其他的函式,需搭配其他函式使用

# 基本裝飾器
# 定義
# def 裝飾器名稱(回呼函式名稱):
#     def 內部函式名稱():
#         # 裝飾器內部程式碼
#         回呼函式名稱()
#     return 內部函式名稱

# 使用裝飾器
# @裝飾器名稱
# def 函式名稱():
#     函式內部的程式碼
# 函式名稱
# ★★★★★執行順序★★★★★
# 1.會先執行裝飾器內部的程式
# 2.再來才是普通函式本來的程式
# ★★★★★執行順序★★★★★

# 範例
# def testDecorator(callback):
#     def innerFunc():
#         print("裝飾器")
#         callback()
#     return innerFunc
#
# @testDecorator
# def decoratedFunc():
#     print("普通函式")
#
# decoratedFunc()

# 範例二,傳遞參數
# def testDecorator(callback):
#     def innerFunc():
#         print("裝飾器")
#         callback(3)
#     return innerFunc
#
# @testDecorator  #先執行裝飾器函數 innerFunc
# def decoratedFunc(data): #傳入decoratedFunc 成callback
#     print("普通函式",data)
#
# decoratedFunc()

# 範例三,
# def myDeco(cb):
#     def run():
#         print("裝飾器中的程式碼")
#         cb("test")
#     return run
# @myDeco
# def test(data):
#     print("哈囉",data)
# test()
#
def calculate(callback):
    def run():
        result = 0
        for n in range(51):
            result += n
        callback(result)
    return run

@calculate
def show(n):
    print("總和為:",n)
#return result #印出1+2+...+50總和
show()


# 單獨執行
def calculate(callback):
    def wrapper(*args, **kwargs):
        result = sum(range(51))
        callback(result)
    return wrapper

@calculate  # 第一層處理
def display1(data):
    print("總和為:", data)
@calculate # 第二層處理
def display2(data):
    print("結果完成:", data)

display1()
display2()
