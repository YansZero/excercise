# 定義建立生成器函式
def test():
    print("階段一")
    yield 5
    print("階段二")
    yield 10

# 呼叫並回傳生成器    
# gen=test()
# print(gen) #但這時候只有生成器

#搭配for 
# for x in  gen:
#     print(x)  #yield 一段一段跑

# 產生無限多偶數
def generatorEven(max):
    number=0
    while number <= max:
        yield number
        number +=2
    # yield number
    # number +=2
    # yield number
    # number +=3
    # yield number
    # number +=7

Evengenerator=generatorEven(10)

for data in Evengenerator:
    print(data)