# def 函式名稱(參數,參數2,....,參數N):
#     函式功能
#     return 回傳值 (注意回傳值 才是這個FUNCTION 最主要的意義)
from unittest import result


def number_add(x1,x2):
    return x1 + x2

def number_sub(x1,x2):
    return x1 - x2

def number_multi(x1,x2):
    return x1 * x2

def number_div(x1,x2):
    if x2==0 :
        return 0
    else :        
        return x1 / x2


value=number_multi(3,4)
print("value is :",value)

value=number_multi(7,8)
print("value is :",value)

# 宣告含有預設值的函式
# def 函式名稱(參數=值1,參數2=值2):
#     函式功能
#     return 回傳值 (注意回傳值 才是這個FUNCTION 最主要的意義)

# 呼叫函式 參數名稱對應資料 可不管順序
# def 函式名稱(名稱1,名稱2):
# 函式名稱(名稱2=3,名稱1=5)

def divide(n1,n2):
    result = n1/n2
    print(result)

divide(2,4)
divide(n2=6,n1=24)

# 無限參數
# def 函式名稱(*無限參數):
# 參數以TUPLE資料型態傳入
def say(*msgs):
    for msg in msgs:
        print(msg)

say("Hello","world","python!")

# 注意某些運算 需要有預設值
def power(base,exp=0):
    print(base**exp)
    return base**exp

power(4,3)
power(4) 

def avg(*nums):
    sum=0
    for n in nums :
        sum += n
    print(sum/len(nums))

avg(1,3,8,8)        