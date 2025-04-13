# Python 時間、時區的操作
# 載入相關的模組 datetime的 time,datetime
# from datetime import time, datetime, timedelta
# 任意時間:年月日時分秒
# d1=datetime(年,月,日,時,分,秒)
# ex: d1=datetime(2025,1,2,3,4,5)
# 當下時間
# now = datetime.now()

# 印出時間物件相關屬性
# print(now.year,now.month,now.day)
# print(now.hour,now.minute,now.second)
# print(now.weekday()) # 0~6 星期一~星期日

# 時間差
# 需引入 datetime的timedelta
# differ1 = timedelta(hours=9)
# differ2 = timedelta(minutes=8)
# differ3 = timedelta(seconds=7)
# 新的時間物件 = 時間物件 +/- 時間差
# 時間差 = 時間物件A - 時間物件B

# 時區操作
# 需引入 datetime的timezone
# 建立時區的物件
# tz1=timezone(timedelta(hours=3))   #時區 +3
# tz2=timezone(timedelta(hours=-16)) #時區 -16
# 使用作業系統的預設時區(根據使用者所在的時區,TPE +8)
# default_now = datetime.now()
# time_1 = datetime(2020,2,3,1,3,5)
# # 設定時區到PDT(太平洋夏令時間-7,與TPE 時間差15小時)
# pdt = timezone(timedelta(hours=-7))
# pdt_now = datetime.now(tz=pdt)
# pdt_time= time_1.astimezone(tz=pdt)
#
# print("default_now(without timezone):",default_now)
# print("time_1:",time_1)
# print("pdt:",pdt)
# print("pdt_now:",pdt_now)
# print("pdt_time:",pdt_time)

from datetime import time, datetime, timedelta, timezone

# 當下時間
now = datetime.now()
print(now)
print("只取得現在的年月日(strftime)", now.strftime("%Y-%m-%d"))
print("只取得現在的時分秒(strftime)", now.strftime("%H-%M-%S"))
print("現在星期幾:", now.weekday())

# 印出8小時候7分鐘的時間資訊(做時間運算)
differ = timedelta(hours=8, minutes=7)
new_time = now + differ
print("new_time(8小時右7分後):", new_time)

# 取得日本時區(+9時區)
jp_tz = timezone(timedelta(hours=9))
jp_time = now.astimezone(tz=jp_tz)
print("日本現在時間:", jp_time.strftime("%Y-%m-%d %H:%M:%S"))
