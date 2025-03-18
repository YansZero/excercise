# File 實體物件的設計:包裝檔案讀取的程式
class File:
    def __init__(self, name):
        self.name = name
        self.file = None

    def open(self):
        self.file = open(self.name, mode='r', encoding='utf-8')

    def read(self):
        return self.file.read()


# 讀取第一個檔案
f1 = File("data1.txt")
f1.open()
data = f1.read()
print(data)

# 讀取第二個檔案
f2 = File("data2.txt")
f2.open()
data2 = f2.read()
print(data2)
