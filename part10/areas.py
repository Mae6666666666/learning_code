

class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        return f"{self.width}x{self.height}"

    def area(self):
        return self.width * self.height

rectangle = Rectangle(2, 3)
print(rectangle)
print("area:", rectangle.area())

class Square(Rectangle):
    def __init__(self, width: int):
        super().__init__(width, width)


square = Square(4)
print(square)
print("area:", square.area())