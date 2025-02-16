import math
n = int(input("sides: "))
l = int(input("length: "))
a = l/2*(math.tan(math.pi/n))
r = (n*l) * (a) * 0.5
print(round(r))