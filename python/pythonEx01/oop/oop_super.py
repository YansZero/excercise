# Python Super 函式

class Rectangle:
    length = 0
    width = 0

    def __init__(self, length, width):
        self.length = length
        self.width = width
        print("這是Rectangle init")


class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
        print("這是Square init")


squareItem = Square(30, 30)


# 正方體 Cube 長*寬*高

class Cube(Square):
    height = 0

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
        print(f"立方體的長寬高{length},{width},{height}")


cube = Cube(10, 10, 10)
