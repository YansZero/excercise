# Python 中的作用域

# 變數範圍與作用域
# 找變數會就近原則
# LEGB 作用域順序
# L- Local
# E- enclosed
# G- Global
# B- Built-in

# 變數範圍
a = 10
print(f"外面的a is:{a}")
def function_a():
    # a 是function_a local變數
    a = 1
    print(f"a is:{a}")

    def function_b():
        # b function_b local變數
        # a function_b enclosed
        b = 2
        print(f"b:{b}")
        print(f"a:{a}")

    function_b()

function_a()
print(f"a={a}")

# built-in
from math import e
print(round(e,4))

def function_c():
    print(f"e is:{e}")

function_c()