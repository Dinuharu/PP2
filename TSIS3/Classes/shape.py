class Shape:
    def init(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def init(self, lenght):
        super().init()
        self.len=lenght
    def area(self):
        return self.len**2
class Rectangle(Shape):
    def init(self, len, w):
        super().init()
        self.len=len
        self.width=w
    def area(self):
        return self.len* self.width