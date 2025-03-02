file_path = r"E:\coding\test\abc.txt"

try:
    with open(file_path, encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print(f"檔案{file_path}不存在")
