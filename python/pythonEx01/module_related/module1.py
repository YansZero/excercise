# python中的if __name__ == '__main__'
# 模組1
# print("模組1__name__ == '__main__'")
#如果要用某個程式為起點,__name__ 會是__main__
import module2 as m2

m2.hello()

print("模組1__name__:"+ __name__)
if __name__ == '__main__':
    print("模組1__name__ == '__main__'")
