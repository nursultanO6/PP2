import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x) 
        print(self.y)
    def move(self, cx, cy):
        self.x = cx
        self.y = cy 
    def dist(self, newp):
        dis = math.sqrt((self.x - newp.x)**2 + (self.y - newp.y)**2)
        return dis
x = int(input())
y = int(input())
p1 = Point(x, y)
nx = int(input())
ny = int(input())
p2 = Point(nx, ny)
p1.show()
p2.show()
print(p1.dist(p2))
