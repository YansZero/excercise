import json

# 因為 file寫入只能字串,所以要寫入其他非字串的 可以轉換成json文字
# import json後 使用json.dump(來源) 即可轉換成文字
# 要注意如果寫入中文 記得要關ascii code關掉 使用json.dumps(str,ensure_ascii=False)
# 不然會變成加密過後的文字
# 範例
# 不使用 ensure_ascii=False, {"a": 123, "b": [1, 2, 3, 4, 5, 6], "c": "\u54c8\u54c8"}
# 使用 ensure_ascii=False, {"a": 123, "b": (1, 2, 3, 4, 5, 6), "c": "哈哈"}
str = {"a": 123, "b": (1, 2, 3, 4, 5, 6), "c": "哈哈"}

file_path = r"E:\coding\test\zzz.txt"

try:
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(json.dumps(str, ensure_ascii=False))
        #json.dump(str,file,ensure_ascii=False )
except Exception as e:
    print(f"寫入有異常,{e}")

# 插入模式 a
new_str = "\n go \n go \n go"
try:
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(new_str)
except Exception as e:
    print(f"寫入有異常,{e}")