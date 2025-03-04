# Python中的方法重寫(Method overriding)

# 動物會吃東西
class Animal:
    def eat(self):
        print("動物正在吃東西")


# 哺乳類 是動物的子類別
# 貓狗是哺乳類的子類別
class Mammal(Animal):
    def hi(self):
        print("我是哺乳類")

    pass


class Cat(Mammal):
    def eat(self):
        print("貓正在吃魚")

    def jump(self):
        print("貓正在跳")

    pass


class Dog(Mammal):
    def eat(self):
        print("狗正在啃骨頭")

    def run(self):
        print("狗正在跳")

    pass


cat = Cat()
dog = Dog()
mammal = Mammal()

cat.eat()
dog.eat()
dog.hi()

mammal.eat()


class Rabbit(Animal):
    def eat(self):
        print("兔子正在吃東西")


animal = Animal()
rabbit = Rabbit()

animal.eat()
rabbit.eat()
