# Python 字串方法
# help(str) 查尋相關範例


# 使用者的全名
name = "jason Tseng 曾帥哥"
print("全名為", name)

length = len(name)
print("全名共有", length, "個字元")

# 找到第一個空格
space_pos = name.find(" ")
print("第一個空格出現在", space_pos, "個字元")

# 尋找特定字串第一次出現的位置
space_where = name.index("Tseng")
print("Tseng在name的位置為", space_where)

# 以" "切割
space_list = name.split(" ")
print("將name用空格切割", space_list)

# Capitalize 將第一個字母變大寫
print("將name第一個字母變大寫", name.capitalize())

# upper 將所有字母變大寫
print("將name全部個字母變大寫", name.upper())

# lower() 將所有字母變小寫
print("將name全部個字母變大寫", name.lower())

# count 計算特定字元個數
phoneNumber = "0987-654-321"
dashCount = phoneNumber.count("-")
print(f"電號號碼{phoneNumber}裡面總共有{dashCount}個'-'")

# replace 取代的文字
textStr = 'abcdxyzDDD'
newStr = textStr.replace("D", "")
print(f"原本字串{textStr},取代D為空格後{newStr}")

# 額外練習
# 使用者名稱不可以超過12個字元
# 使用者名稱不可以包含空格
# 使用者名稱不可以包含數字
# 都符合的話，顯示歡迎+使用者名稱
# string.isalpha() =>是否由字母組成
# string.isalnum() =>是否由字母或者數字組成

userName = input("請輸數使用者的名稱: ")
if len(userName) > 12:
    print("你的使用者名稱長度超過12個字元")
elif userName.find(" ") >= 0:
    print("你的使用者名稱不可以包含空格")
elif userName.isalnum() and not userName.isdigit():
    print(f"你的使用者名稱不可以包含數字")
elif not userName.isalpha():
    print(f"你的使用者名稱不可以包含數字")
else:
    print(f"歡迎{userName}")
