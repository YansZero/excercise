# Python 生成器 Generator
# 動態產生可迭代的資料,搭配for迴圈使用
# 函式 使用 yield,呼叫時回傳生成器
# 基本語法
# yield 任何型態的資料

# def 函式名稱():
#     yield 資料 (可以使用yield多次)
# 呼叫函式,回傳生成器
# 變數名稱=函式名稱

# ex
# def test():
#     yield 3
## 呼叫函式,回傳生成器
# gen = test()
## 搭配for迴圈使用
# for data in gen:
#     print(data)

# ex2
# def test():
#     yield 3
#     yield 5
# # 呼叫函式,回傳生成器
# gen = test()
# # 搭配for迴圈使用
# for data in gen:
#     print(data)

# 產生 Fibonacci 數列
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        print("a=", a)
        print("b=", b)
        yield a
        a, b = b, a + b


for num in fib(5):
    print(num)

print(f"Fibonacci 數列產生器 fib(3) ")  # 0
gen = fib(3)
# 搭配next()使用 (手動控制)
print(f"Fibonacci 數列產生器使用next {next(gen)}")  # 0
print(f"Fibonacci 數列產生器使用next {next(gen)}")  # 1
print(f"Fibonacci 數列產生器使用next {next(gen)}")  # 1


def generateEven():
    number = 0
    yield number
    number += 2
    yield number
    number += 2
    yield number


print(f"使用多重yield的產生器")
evenGenerator = generateEven()
for data in evenGenerator:
    print(data)  # 結果為 0, 2, 4


# 產生小於某個數字的偶數生產器
def generate_even_with_count(count):
    number = 0
    while number < count:
        yield number
        number += 2


print(f"產生小於某個數字的偶數生產器")
generate_even_list = generate_even_with_count(17)

for even in generate_even_list:
    print(even)
