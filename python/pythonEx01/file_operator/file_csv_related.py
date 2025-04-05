# Python csv檔案寫入讀取相關
# 載入csv 模組
# 使用 with open("file_path", "w", newline=""),newline 來避免不必要的資料寫入
# csv.writer(檔案) 來控制相關操作
# writer.writerow([data,data2,...]) 寫入每列的資料
import csv

file_path = r".\test_csv.csv"
# 寫入csv檔案
with open(file_path, "w", newline="",encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([{"apple": 123}, {"banana": 2}, {"melon": 3}])
    writer.writerow([1, 2, 3])
    writer.writerow([4, 5, 6])
    writer.writerow([7, 8, 9])
    writer.writerow(["a", "b", "c"])
    writer.writerow(["今天", "天氣", "下雨"])

# 讀入csv檔案
# with open(file_path, "r", newline="",encoding="utf-8") as csv_file:
# 搭配encoding="utf-8" 避免字串編碼有錯誤
# reader = csv.reader(檔案) 將放入變數 能進行讀取操作
with open(file_path, "r", newline="", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    # 逐列讀取資料(list形式,每列是字串形式)
    total=0
    for row in reader:
        print(row)
        for col in row:
            if col.isdecimal():
                total+= int(col) #轉換成整數
            else:
                continue
    print(f"csv內有數字的加總為 {total:>10.2f}")