
n1=int(input("請輸入數字一: "))
n2=int(input("請輸入數字二: "))

op=input("請輸入要做的運算(+,-,*,/): ")

if op =='+':
    result = n1 + n2
elif op =='-':
    result = n1 - n2
elif op =='*':
    result = n1 * n2
elif op =='/':
    if n2==0:
        result = "數字二必須不等於0!"
    else :    
        result = n1/n2
else :    
    result = "不支持的運算方式!"

print(result)