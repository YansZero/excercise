# Python 計算機程式

operator = input("請輸入運算符號(+,-,*,/)")
num1 = float(input("請輸入第一個數字:"))
num2 = float(input("請輸入第二個數字:"))
result = 0
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    print("運算符無效!")

print(f"運算結果為:{result}")
