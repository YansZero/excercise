# Python中的集合 list,sets與tuple

# list 列表,有序且可變的集合,用於需要保持順序並且可能需要修改的數據
# [] 中括號

fruits = ["apple", "banana", "lemon"]

print(fruits[1])

for fruit in fruits:
    print(f"the fruit is: {fruit}")

# add some item
fruits.append("orange")
print(fruits)

# remove some item
fruits.remove("banana")
print(fruits)

# find index
print(fruits.index("lemon"))

# list can add multiple same item
fruits.append("apple")
fruits.append("apple")
print(fruits)

fruits2 =[1,2,3,4]
# 可以使用 list.extend(另外一個可迭代的), 從最後面擴充
fruits.extend(fruits2)
print(f"fruits使用extend加入fruits2後:{fruits}")

# count 計算總數
print(f"List apple 總數為:{fruits.count("apple")}")

# reverse 反轉LIST
fruits.reverse()
print(f"List 反轉後: {fruits}")

# set 無序且元素唯一的集合
# {} 大括號

fruits_set = {"apple", "banana", "guava"}
fruits_set.add("apple")
for item in fruits_set:
    print(f"set元素:", item, end="\n")

if "apple" in fruits_set:
    print("set中有apple")
else:
    print("set中沒有apple")

# tuple 元組 有序且不可變的集合, 適用於不需要修改的數據
animals = ("cat", "dog", "pig", "cat")
print(f"tuple animals中cat,總元素為{animals.count("cat")}")

# tuple 不可以加入元素,只能重新宣告
# animals.add("xxx")
