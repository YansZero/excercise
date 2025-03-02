# 使用Python 進行檔案偵測
import os as o
import os.path

# 檔案位置:E:\coding\test
# 使用 r 讓\顯示出來, 或者多加一個顯示
file_path = r"E:\coding\test"
file_path2 = "E:\\coding\\test\\abc"
print(file_path)
# file = fileinput

# 檢查路徑是否存在
file = o.path.exists(file_path)
file2 = o.path.exists(file_path2)

print(f"路徑{file_path},是否存在:{file}")
print(f"路徑{file_path2},是否存在:{file2}")

# 檢查是否為檔案 o.path.isFile
# str = r"E:\coding\test\abc.txt"
str = r"E:\coding\test\abc\abc.txt"
if os.path.isfile(str):
    print(f"{str}為檔案")
elif os.path.isdir(str):
    print(f"{str}為目錄")
else:
    print("其他的可能性")
