# class 類別名稱:
#     定義初始化函式
#     def __init__(self,參數):
#         透過操作self 來定義實體屬性
# 建立實體物件 放數變數 obj中
# obj=類別名稱() #呼叫初始化函式        
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(3, 4)
print(p1.x, p1.y)
p2 = Point(5, 6)
print(p2.x, p2.y)


class FullName:
    def __init__(self, lastName, firstName):
        self.first = firstName
        self.last = lastName


name1 = FullName("Jason", "Tseng")
print(name1.last, name1.first)
name2 = FullName("Lisa", "Hsiao")
print(name2.last, name2.first)


# 實體物件.實體方法
# def 方法名稱(self,參數)
# class FullName2:
#     def __init__(self,lastName,firstName):
#         self.first = firstName
#         self.last  = lastName

#     def show(self):
#         print(self.last,self.first)    

# name1=FullName2("Jason","Tseng")
# # print(name1.last ,name1.first)
# name1.show()
# name2=FullName2("Lisa","Hsiao")
# name2.show()
# print(name2.last ,name2.first)

class File:
    # 初始化函式
    def __init__(self, name):
        self.name = name
        self.file = None  # 尚未開啟檔案:初期是None

    # 實體方法
    def open(self):
        self.file = open(self.name, mode="r", encoding="utf-8")

    def read(self):
        return self.file.read()

    # 讀第一個檔案


f1 = File("data1.txt")
f1.open()
data = f1.read()
print(data)

# 讀第二個檔案
f2 = File("data2.txt")
f2.open()
data2 = f2.read()
print(data2)
