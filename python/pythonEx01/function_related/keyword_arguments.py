# Python 關鍵字參數 Keyword Arguments
# 利用關鍵字鎖定參數來避免參數傳入錯誤,
# 可以不管順序

# def hello(greeting, title, first_name, last_name):
#     print(f"{greeting},{title},{first_name},{last_name}")

# hello("你好", "Dr", "Apple", "Chen")
#
# hello(greeting="您好", title="Mr", first_name="小寶", last_name="韋")

def get_number(country_code,area_code,first,last):
    return f"{country_code}-{area_code}-{first}-{last}"

number_str= get_number(country_code="886",area_code="04",first="9876",last="5432")
print(number_str)