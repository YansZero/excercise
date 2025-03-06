# Python function
# 稱為method

def say_hello():
    print("你好")


# 傳遞參數,方法括號內加入傳遞參數
def greeting(name):
    print(f"您好 {name}")


say_hello()
greeting("cat")


def calculator_sum(para, para2):
    return para + para2


def calculator_subtract(para, para2):
    return para - para2


def calculator_multi(para, para2):
    return para * para2


def calculator_divide(para, para2):
    return 0 if para2 == 0 else para / para2


print(f"+計算結果為{calculator_sum(1, 2)}")
print(f"-計算結果為{calculator_subtract(5, 1)}")
print(f"*計算結果為{calculator_multi(6, 7)}")
print(f"/計算結果為{calculator_divide(8, 1.5):.2f}")


def create_name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return first_name + " " + last_name


name = create_name("tommy", "chang")
print(name)

# function 內傳遞參數也可以先聲明哪個參數要先哪些值
# 可以不管排序, 詳情請看keyword_arguments.py
name2 = create_name(last_name="chen", first_name="jimmy")
print(name2)
