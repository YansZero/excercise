# 裝飾器工廠
# 三層函式
# def 裝飾器工廠名稱(參數名稱,....):
#     def裝飾器名稱(回呼函式名稱):
#         def 內部函式名稱():
#             #裝飾器內部的程式碼
#             回呼函示名稱()
#         return 內部函式名稱    
#     return 裝飾器名稱       
# 用法:
# @裝飾器工廠名稱(參數資料,....)
# def函式名稱():
#     #函式內部的程式碼

#  函式名稱() #呼叫帶有裝飾器的函式名稱

# def testFactory(base):
#     def testDecorator(callback):
#         def innerFunc():
#             result=base*3
#             callback(result)
#         return innerFunc    
#     return testDecorator

# @testFactory(3)    
# def decoratedFunc(result):
#     print("普通函式",result)

# decoratedFunc()

def sumFactory(target):
    def calculate(callback):
        def run():
            total = 0
            for n in range(target+1):
                total += n
            callback(total)    
        return run
    return calculate

@sumFactory(100)           
def show(result):
    print('結果是:',result)

@sumFactory(50)           
def showEnglish(sum):
    print('sum is',sum)


show()    
showEnglish()