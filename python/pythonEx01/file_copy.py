# 使用Python複製檔案

import shutil

# 要注意此module 不會幫忙建立資料夾
# shutil.copyfile() -- 只複製文件內容 不複製文件描述的資訊
# shutil.copy() -- 類似copyfile, 可針對資料夾使用,但資料夾要存在
# shutil.copy2() -- 複製內容, 可針對資料夾使用,但資料夾要存在
basic_path = r"E:\coding\test"
source_path = f"{basic_path}/zzz.txt"
dest_path = f"{basic_path}/copy.txt"
dest_path2 = f"{basic_path}\\test\\"
dest_path3 = f"{basic_path}\\test2\\"

shutil.copyfile(source_path, dest_path)
shutil.copy(source_path, dest_path2)
shutil.copy2(source_path, dest_path3)
