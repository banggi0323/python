class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f'({self.x}, {self.y})')

    def set(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return (self.x, self.y)

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.left = Point(x1, y1)
        self.right = Point(x2, y2)

    def show(self):
        print(f'좌측 상단 꼭지점이 ({self.left.x}, {self.left.y})이고 우측 하단 꼭지점이 ({self.right.x}, {self.right.y})인 사각형입니다.')

    def getWidth(self):
        return self.right.x - self.left.x

    def getHeight(self):
        return self.right.y - self.left.y

    def getArea(self):
        return self.getWidth() * self.getHeight()

    def getPerimeter(self):
        return 2 * (self.getWidth() + self.getHeight())


r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
