# python 字典 dic

# key => value

capital = {
    "United States": "Washington DC",
    "Japan": "Tokyo",
    "France": "Paris",
    "ROC": "Taipei"
}

# get() 取得鍵值對應的值
print(capital.get("ROC"))
print(capital.get("France"))

# update() 更新鍵值的值
capital.update({"Germany": "Berlin"})
print(capital)

# pop() 刪除鍵值對
capital.pop("ROC")
print(capital)

# values 取得所有值
print("values所有值為",capital.values())

# items 取得所有鍵值對
print("items for capital",capital.items())