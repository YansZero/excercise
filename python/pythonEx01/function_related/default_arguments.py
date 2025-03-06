# 函式的預設引入(default arguments)
# 可以減少參數傳入 讓fun簡潔
# 預設參數需要寫在後面

def greet(name,greeting="Hello"):
    print(f"{greeting},{name}")

greet("Tom")

greet("Tom","Good Morning")