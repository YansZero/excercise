# Duck typing

class Duck:
    def walk(self):
        print("鴨子在走路")

    def talk(self):
        print("鴨子在呱呱呱")


class Chicken:
    def walk(self):
        print("雞在走路")

    def talk(self):
        print("雞在咕咕咕")
        print("雞在亂走")

    def run(self):
        print("雞在跑步")


# 即使沒有繼承的關係,也可以當作同一類型的類別使用
# 有類似的method name
# 如果有同樣的行為可以視為同一物件

class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()



duck = Duck()
person = Person()
person.catch(duck)

chicken = Chicken()
person.catch(chicken)
