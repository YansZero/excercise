# Python中的map

# map(函式,可迭代的[列表])

# store = [
#     ('襯衫', 20), #美金
#     ('褲子', 30),
#     ('夾克', 50),
#     ('襪子', 10)
# ]
#
# to_europe = lambda data: (data[0], data[1] * 0.82)
# to_ntd = lambda data: (data[0], data[1] * 30)
#
# store_euros = list(map(to_europe, store))
# store_tw = list(map(to_ntd, store))
# print(f"歐洲商店價格{store_euros}")
# print(f"台灣商店價格{store_tw}")

store = [
    ('襯衫', 600),  # NTD
    ('褲子', 900),
    ('夾克', 1500),
    ('襪子', 300)
]
print(f"台灣商店價格{store}")
to_usd = lambda data: (data[0], round(data[1] / 30))
store_usd = list(map(to_usd, store))

print(f"美國商店價格{store_usd}")

for item in store_usd:
    print(item)

#使用filter + map with lambda
store_tw = [
    ('襯衫', 600),  # NTD
    ('褲子', 900),
    ('夾克', 1500),
    ('襪子', 300)
]
to_filter_lambda = lambda data: filter(lambda data2: data2[1] > 700, data)
to_map_lambda = lambda data: map(lambda data2: (data2[0], round(data2[1] / 30)), to_filter_lambda(data))
print(list(to_map_lambda(store_tw)))
