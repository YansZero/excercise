# 回呼函式 callback function
# 透過參數傳遞函式到另一個函式中

# EX:
# def test(arg):
#     arg(50)  #呼叫回呼函式，可帶入參數

#定義一個回呼函式
# def handle(data):
#     print(data) 

# test(handle)       


# def add(n1,n2,cb):
#     cb(n1+n2)

# def handle1(result):
#     print("結果是:",result)

# def handle2(result):
#     print("Result of Add is :",result)

# add(3,4,handle1)    
# add(5,6,handle1)    
# add(4,2,handle2)  

#回撥函式1
#生成一個2k形式的偶數
def double(x):
    return x * 2
    
#回撥函式2
#生成一個4k形式的偶數
def quadruple(x):
    return x * 4

#中間函式
#接受一個生成偶數的函式作為引數
#返回一個奇數
def getOddNumber(k, getEvenNumber):
    return 1 + getEvenNumber(k)    

#起始函式，這裡是程式的主函式
def main():    
    k = 1
    #當需要生成一個2k+1形式的奇數時
    i = getOddNumber(k, double)
    print(i)
    #當需要一個4k+1形式的奇數時
    i = getOddNumber(k, quadruple)
    print(i)
    #當需要一個8k+1形式的奇數時
    i = getOddNumber(k, lambda x: x * 8)
    print(i)
    
if __name__ == "__main__":
    main()    