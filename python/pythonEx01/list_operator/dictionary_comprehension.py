# Python中的字典推導式(dictionary comprehension)

# dictionary
# {key: expression for key, value in iterable}
# {key_expr: value_expr for 變數 in 可迭代對象 if 條件}
# 適用場景: 產生字典，如鍵值對變換、篩選等
# 溫度運算
cities_in_f = {'LA': 120, 'New York': 65, 'Chicago': 50, 'Miami': 150}
cities_in_c = {key: round((value - 32) * 5 / 9) for key, value in cities_in_f.items()}
print(cities_in_f)
print(cities_in_c)

# ex2 條件判斷
weather = {
    '台北': '大晴天', '台中': '大晴天', '台南': '下雨', '高雄': '下雨', '屏東': '烏雲'
}

sunny_weather = {key: value for key, value in weather.items() if value == '大晴天'}
print(weather)
print(sunny_weather)

# ex3 條件判斷 + 函式
cities_in_us = {'LA': 120, 'New York': 65, 'Chicago': 30, 'Miami': 150}
def check_temp(value):
    if value >= 70:
        return '熱'
    elif value >= 40:
        return '暖'
    else:
        return '冷'


description_cities = {key: check_temp(value) for key, value in cities_in_us.items()}
print(description_cities)
