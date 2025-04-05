# Python 日期操作
# 匯入datetime模組的date
from datetime import date, timedelta

# 取得特定日期 date(年,月,日)
date1 = date(2021, 1, 2)
date2 = date(2022, 2, 2)
# 當下日期 date.today()
date3 = date.today()
print(f"日期1:{date1},日期2:{date2},日期3:{date3}")

# 日期物件代表的年,月,日,星期(0~6)
print(f"{date3.year},{date3.month},{date3.day},{date3.weekday()}")

# 取得當前日期時間,沒給時間就是當天開始
date4 = date.ctime(date3)
print(date4)
# 日期格式 date物件.strftime(日期格式)
date5 = date3.strftime("%Y/%m/%d")
print(date5)

# 建立代表10天的時間差物件
differ1 = timedelta(days=10)
# 建立代表1星期的時間差物件
differ2 = timedelta(weeks=1)

# 新的日期物件 = 日期物件 +- 時間差
# 時間差 = 日期物件 - 日期物件2
date6 = date3 + differ1
date7 = date3 - differ2
print(f"date3 + differ1 {date6}")
print(f"date3 - differ2 {date7}")
print(f"時間差(date6 - date7)={date6 - date7}")

# 列印出往後一週的日期
print(f"下禮拜{date.today() + timedelta(weeks=1)}")

# 列印出當前月份所有日期以及星期幾
today = date.today()
month_first_date = date(today.year, today.month, 1)
weekdays_names = {0: "週一", 1: "週二", 2: "週三", 3: "週四", 4: "週五", 5: "週六", 6: "週日"}

while month_first_date.month == today.month:
    print(month_first_date, weekdays_names[month_first_date.weekday()])
    month_first_date = month_first_date + timedelta(days=1)
