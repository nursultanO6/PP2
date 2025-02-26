from functools import reduce
lst = [1, 2, 3]
num = reduce(lambda x, y: y*x, lst)
print(num)