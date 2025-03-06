# 型別轉換 type casting

name = "Jason"
age = 30
score = 100.00
student = True

# 顯示型別(直接指定型別轉換) 使用type(變數名稱) 顯示型別名稱
print(f"name 的型別是: {type(name)} ")
print(f"age 的型別是: {type(age)} ")
print(f"score 的型別是: {type(score)} ")
print(f"student 的型別是: {type(student)} ")

print("--------開始顯示型別轉換---------------")
age = float(age)
print(f"age 轉換行別後值為: {age} ,型別為: {type(age)}")

score = int(score)
print(f"score 轉換行別後值為: {score} ,型別為: {type(score)}")

student = str(student)
print(f"student 轉換行別後值為: {student} ,型別為: {type(student)}")

print("--------結束顯示型別轉換---------------")

# 隱式型別轉換(不特別聲明怎樣轉換,讓系統自己轉換)
print("--------開始隱式型別轉換---------------")
x = 10
y = 2.0
print(f"x值為{x},型別為{type(x)}")
print(f"y值為{y},型別為{type(y)}")
x = x / y
print(f"x新的值為{x},型別為{type(x)}")
print("--------結束隱式型別轉換---------------")

