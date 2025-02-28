# args => arguments 任意數量的參數 * => 被打包tuple
# kwargs => 關鍵字 + args 任意數量關鍵字的參數 ** => 被打包dictionary

# 沒使用*args
def add(a, b):
    return a + b
print(add(1,2))

# 使用*args
def add_multi(*args):
    total = 0
    for arg in args:
        print(f"arg is:{arg}")
        total += arg
    return total

print(add_multi(5,6))
print(add_multi(5,6,7,8))

# kwargs 範例
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"key:{key},value:{value}")

print_info(name="JoJo",age=25,description="是個工程師")