# Python 裝飾器工廠 decorator factory
# def 裝飾器工廠名稱(參數名稱,....)
#     def 裝飾器名稱(回呼函式名稱)
#         def 內部函式名稱():
#             裝飾器內部的程式碼
#             回呼函式名稱()
#         return  內部函式名稱
#     return 裝飾器名稱

# 用法
# @裝飾器工廠名稱(參數名稱,....)
# def 函式名稱()
#     函式內部的程式碼
# 函式名稱()

# def testFactory(base):
#     print("裝飾器工廠")
#     def testDecorator(callback):
#         def innderFunc():
#             print("裝飾器",base)
#             callback()
#         return innderFunc
#     return testDecorator
#
# @testFactory(3)
# def decoratedFunc():
#     print("普通函式")
# decoratedFunc()

def testFactory(base):
    print("裝飾器工廠")
    def testDecorator(callback):
        def innderFunc():
            result = base *3
            callback(result)
        return innderFunc
    return testDecorator

@testFactory(3)
def decoratedFunc(result):
    print("普通函式",result)

decoratedFunc()


# 心得
# 多個裝飾器：如果你要在每個裝飾器中處理不同的功能（例如多個 callback），那就必須使用多層裝飾器，也就是「一層一層包裝」。每個裝飾器會「獨立包裝」被裝飾的函式，這樣就能完成你想要的功能，並且可以分開處理。
# 合併為一個裝飾器：如果你希望讓所有邏輯都在同一個裝飾器內處理，且支援多個 callback，那就必須使用三層 def 來構建這個裝飾器。這樣可以讓你一次性傳入多個參數（例如多個 callback 函式），並且統一處理所有邏輯。
# 1. 多個裝飾器（每個做一個功能，兩層）
# 假設你有兩個 callback 函式，想分開處理：
#
# def calculate(callback):
#     def decorator(cb):
#         def wrapper(*args, **kwargs):
#             result = sum(range(51))
#             callback(result)
#             return cb(*args, **kwargs)
#         return wrapper
#     return decorator
#
# def display1(data):
#     print("總和為:", data)
#
# def display2(data):
#     print("結果完成:", data)
#
# @calculate(display1)  # 第一層處理
# @calculate(display2)  # 第二層處理
# def run():
#     print("任務執行中")
# run()
#
# 2. 合併為一個裝飾器（三層）
# 如果你想合併所有邏輯到同一個裝飾器中，就可以像這樣寫：
# def calculate(callback1, callback2):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             result = sum(range(51))
#             callback1(result)  # 第 1 個 callback
#             callback2(result)  # 第 2 個 callback
#             return func(*args, **kwargs)  # 執行原本的函式
#         return wrapper
#     return decorator
#
# def display1(data):
#     print("總和為:", data)
#
# def display2(data):
#     print("結果完成:", data)
#
# @calculate(display1, display2)  # 單一裝飾器處理多個 callback
# def run():
#     print("任務執行中")
# 這樣寫的好處是，只有一層裝飾器，裡面就處理了所有的邏輯（包括兩個 callback 的觸發）。所有的 callback 邏輯都集中在同一個裝飾器中，簡化了結構。
# 🔄 總結：
# 多個裝飾器（兩層 def）：每個裝飾器分開處理各自的功能，最終以「一層層」包裝函式。
# 單一裝飾器（三層 def）：所有邏輯集中在一個裝飾器中，內部可以處理多個 callback。

# 從1+2+3+....+n的裝飾器
def calculate_factory(max):
    def calculate_sum(callback):
        def run():
            result = sum(range(max+1))
            callback(result)
        return run
    return calculate_sum

@calculate_factory(100)
def show(result):
    print("結果是", result)

@calculate_factory(10)
def show_english(result):
    print("result is:", result)

show()
show_english()

# @calculate_sum
# def show(result):
#     print("結果是",result)
#
# @calculate_sum
# def show_english(result):
#     print("result is",result)
#
# show()
# show_english()