# OOP Python中的繼承

class Animal:
    alive = True

    def __init__(self, name, kind, age):
        self.name = name
        self.kind = kind
        self.age = age

    def walk(self):
        print(f"{self.name}正在走路")

    def eat(self):
        print(f"{self.name}正在吃東西")

    def sleep(self):
        print(f"{self.name}正在睡覺")


# 兔子 繼承 Animal

class Rabbit(Animal):
    def jump(self):
        print(f"{self.name}正在跳")


animal = Animal("小黑", "狗", 10)
rabbit = Rabbit("彼得", "兔子", 2)

animal.walk()
rabbit.walk()
rabbit.jump()

class Fish(Animal):
    def swim(self):
        print("魚正在游泳")

class Hawk(Animal):
    def fly(self):
        print("老鷹正在飛")

fish = Fish("魚魚","鯊魚",1)
hawk = Hawk("阿飛","老鷹",10)

fish.swim()
hawk.fly()



