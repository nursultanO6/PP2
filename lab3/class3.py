class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
pl = int(input())
pw = int(input())
p1 = Rectangle(pl,pw)
print(p1.area())