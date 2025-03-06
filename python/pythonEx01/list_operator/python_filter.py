# Python中的filter 過濾

# 可用來過濾可迭代的資料結構(list,...)
# filter(函式,迭代資料結構)
friends = [
    ("Bob", 18),
    ("Steven", 17),
    ("Michael", 19),
    ("Susan", 16)
]

age_filter = lambda data: data[1] >= 18
car_drink_friend = list(filter(age_filter, friends))

for friend in car_drink_friend:
    print(f"{friend[0], friend[1]}")
