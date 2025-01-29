class Stringf:
    def __init__(self, name):
        self.name = name.upper()
p1 = input()
p2 = Stringf(p1)
print(p2.name)