# Python中的Zip函式
# zip 會取數量少的為基準,多餘的不理
# zip 只能被迭代一次, 後面轉會就會成空的
userNames = ["Bob", "Steven", "Sam"]
passwords = ("123", "321", "555", "666")
births = ['1998-02-05', '1998-03-05', '1998-05-05']

# users = zip(userNames, passwords)
users = zip(userNames, passwords, births)
users_a = zip(userNames, passwords, births)
users_b = zip(userNames, passwords)

print(users)
for i in users:
    print(i)
# 轉成list
print(list(users_a))
# 轉成diction
user_dict = dict(users_b)
print(user_dict)

for key, value in user_dict.items():
    print(f"{key}:{value}")


# 使用zip 行列元素互換
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(a)  #原本[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(list(zip(*a))) #結果[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
# 若想得到[[1, 4, 7], [2, 5, 8], [3, 6, 9]]的結果怎麼辦呢?
# 向右旋轉
# [                    [
#   [1,2,3],             [7,4,1],
#   [4,5,6],    =>       [8,5,2],
#   [7,8,9]              [9,6,3]
# ]                    ]
# 譬如假設你今天拍了一張照片存在電腦上，
# 對照片「向左旋轉90度」及「向右旋轉90度」都算蠻常見的操作，
# 而照片可以把它想成是一個二維陣列，
# 因此，旋轉一張照片也就是旋轉一個矩陣的操作了。
#
# 「向右旋轉90度」有蠻多方法可以解的，
# 其中一種是先把圖片上下翻轉，再做行列互換，
# 是可以達到向右旋轉的效果的，
# 123 (上下翻轉)  789  (行列互換)    741
# 456     =>     456      =>      852
# 789            123              963

def rotateRight(arr):
    new_arr = arr[::-1]  # 利用切片上下翻轉
    return list(map(list, (zip(*new_arr))))  # 行列互換，再利用map函數將zip內的元組轉列表


print("旋轉前")
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for item in arr:
    print(item)

print("向右旋轉後")
after_rotate_arr = rotateRight(arr)
for item in after_rotate_arr:
    print(item)

# 向左旋轉
# 原本
# 123
# 456
# 789
# 向左旋轉
# 369
# 258
# 147
print("向左旋轉前")
arr2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for item in arr2:
    print(item)


def rotateLeft(arr):
    newArr = list(map(list, zip(*arr)))
    return newArr[::-1] #倒著印就好


print("向左旋轉後")
after_rotate_left_arr = rotateLeft(arr)
for item in after_rotate_left_arr:
    print(item)
