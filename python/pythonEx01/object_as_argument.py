class Car:
    color = None


def change_color(car, color):
    car.color = color


car = Car()
car2 = Car()
car3 = Car()

print(f"Car  color:{car.color}")
print(f"Car2 color:{car2.color}")
print(f"Car3 color:{car3.color}")

change_color(car,"red")
change_color(car2,"blue")
change_color(car3,"yellow")

print(f"Car  color:{car.color}")
print(f"Car2 color:{car2.color}")
print(f"Car3 color:{car3.color}")
