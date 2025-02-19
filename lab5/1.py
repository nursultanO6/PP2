import re
txt_file = 'test.txt'
with open(txt_file, 'r') as file:
    textm = file.read()

inp = input()
pattern = r'^a*b*$'
result = bool(re.fullmatch(pattern, inp))
print(result)