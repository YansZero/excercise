# 10分鐘學會 Python 物件導向OOP

# 物件(Object)是類別(Class)的實例(Instance)

# Car 4個輪子
# car.bow

# 車 => 類別 Class
# 每一台產生的車子 => 物件 Object

class Car:
    def __init__(self, manufacture, model, year, color):
        # 初始化
        self.manufacture = manufacture
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"{self.model}正在行駛")

    def stop(self):
        print(f"{self.model}停止行駛")


car1 = Car("Toyota", "Altis", 2024, "藍色")
car2 = Car("Nissan", "Sentra 180", 1991, "銀色")

print(f"第一台車是{car1.manufacture},型號:{car1.model},顏色:{car1.color},年份:{car1.year}")
print(f"第一台車是{car2.manufacture},型號:{car2.model},顏色:{car2.color},年份:{car2.year}")
car1.drive()
car2.drive()
car2.stop()
