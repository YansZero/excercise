# 使用python刪除檔案
import os
import shutil
import shutil as s

file_root = r"E:\coding\test"
file_path = f"{file_root}/123.txt"
# 刪除檔案, os.remove
# 檔案必須存在不然會報錯 FileNotFoundError
# 可用try except來接住例外 或者先判斷檔案是否存在 再刪除
try:
    os.remove(file_path)
except FileNotFoundError:
    print(f"檔案:{file_path}不存在")
# 第二種方法
if os.path.isfile(file_path):
    os.remove(file_path)
else:
    print(f"檔案:{file_path}不存在,無法刪除")

# 刪除資料夾,os.rmdir
# 但這方法要空資料夾,避免使用者誤刪
# 會跳出 OSError: [WinError 145] 目錄不是空的

file_dir = r"E:\coding\test\test3"
if os.path.exists(file_dir):
    print(f"資料夾:{file_dir}存在,可刪除")
    os.rmdir(file_dir)
else:
    print(f"資料夾:{file_dir}不存在,無法刪除")

# 刪除資料夾及其內容
# shutil.rmtree,使用要小心
# file_dir4 = r"E:\coding\test\test2"
# shutil.rmtree(file_dir4)

# 刪除資料夾及其內容
# 使用套件 send2trash
# 要確保東西存在,不然會報錯

import send2trash

file_dir5 = r"E:\coding\test\test2"
file_pathA = r"E:\coding\test\456.txt"
try:
    send2trash.send2trash(file_dir5)
except WindowsError or FileNotFoundError:
    print(f"來源資料夾{file_dir5}不存在,無法刪除")

try:
    send2trash.send2trash(file_pathA)
except WindowsError or FileNotFoundError:
    print(f"來源檔案{file_pathA}不存在,無法刪除")
