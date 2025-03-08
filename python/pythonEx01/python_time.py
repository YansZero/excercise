# Python中的time

# 系統的初始時間 ctime
import time

print(time.ctime(0))
print(time.time())

localTime= time.localtime()
print(localTime)
print("格式化的時間",time.strftime("%Y-%m-%d %H:%M:%S.%z",localTime))

time_str = "2025-03-18 12:34:56"
time_obj = time.strptime(time_str,"%Y-%m-%d %H:%M:%S")
print(time_obj)
