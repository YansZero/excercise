# python中的if __name__ == '__main__'
# 模組2
# print("模組2__name__ == '__main__'")
import module1 as m1

print("模組2__name__:" + __name__)
if __name__ == '__main__':
    print("模組2__name__ == '__main__'")


def hello():
    print("hello from module2")
