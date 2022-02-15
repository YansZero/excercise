# 定義裝飾器
# def裝飾器名稱(回呼函式名稱):
#     def 內部函式名稱():
#         #裝飾器內部的程式碼
#         回呼函示名稱()
#     return 內部函式名稱    
# 用法:
# @裝飾器名稱
# def函式名稱():
#     #函式內部的程式碼

# 函式名稱() #呼叫帶有裝飾器的函式名稱
# ex
# def myDeco(cb):
#     def run():
#         print("裝飾器中的程式碼")
#         cb(5)#這個回呼函式，其實就是被裝飾的普通函式
#     return run

# # 使用裝飾器
# @myDeco
# def test(n):
#     print("普通函式的程式碼",n)        

# # => 再沒有裝飾器情況下 類似 test=myDeco("test")
# test()   
 
#定義一個裝飾器 計算1+2+3+...+50 的總和


def caculate(callback):
    def run():
        result=0
        for n in range(51):
            result += n
        # print(result)  
        # 把最後結果透過參數傳到被裝飾的普通函式中  
        callback(result)
    return run

@caculate
def show(n):
    print("最後總合:",n)        

@caculate
def showEnglish(n):
    print("Result is :",n)   
#可以不斷重複使用裝飾內的函式

show()    
showEnglish()