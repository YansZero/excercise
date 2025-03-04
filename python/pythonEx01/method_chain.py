# Python中的方法鏈
# 想達成的的效果
# car.turn_on().drive().brake().turn_off()
# 只要方法中回傳self就可以當作下次呼叫的起點

class Car:
    def turn_on(self):
        print("你啟動了引擎")
        return self

    def drive(self):
        print("你踩了油門")
        return self

    def brake(self):
        print("你踩了煞車")
        return self

    def turn_off(self):
        print("你關閉了引擎")
        return self


car = Car()
car.turn_on().drive().brake().turn_off()
