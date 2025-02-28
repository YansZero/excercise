# Python 中 例外處理(Error handling處理)

# 使用 try catch

try:
    x = int(input("請輸入第一個整數:"))
    y = int(input("請輸入第二個整數:"))
    print(x / y)
# except ValueError:
#     print("輸入錯誤,請輸入整數")
# except ZeroDivisionError:
#     print("被除數不可以為0")
# except (ValueError,ZeroDivisionError):
except ValueError:
    print("ValueError-輸入錯誤,請重新輸入")
except Exception:
    print("額外的錯誤則會到這邊")
else:
    print("else-執行完則會到這邊")
finally:
    print("finally-無論是否出現異常,都會出現")
