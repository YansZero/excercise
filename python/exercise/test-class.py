# 定義類別 與類別屬性(封裝在類別中的變數和函式)
# 定義類別 IO 有兩個屬性supportedSrcs、read
class IO:
    supportedSrcs=["console","file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not Supported!")
        else:            
            print("Read from",src)

print(IO.supportedSrcs)
IO.read("file")
IO.read("InterNet")