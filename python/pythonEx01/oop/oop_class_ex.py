# Python 中的類別變數
class Car:
    wheels = 4

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


car = Car("Ford", "Focus", 2023, "白色")

print("車子輪數為:", car.wheels)

# 將原本的值 改掉就好
car2 = Car("SYM", "勁戰", 2024, "黑色")
print("第二台原本車子輪數為:", car2.wheels)
car2.wheels = 2
print("第二台後來車子輪數為:", car2.wheels)
