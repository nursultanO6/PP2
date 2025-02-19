import re
txt_file = 'test.txt'
with open(txt_file, 'r') as file:
    textm = file.read()

inp = input()
pattern = r'^[a-z]*_[a-z]*$'
result = bool(re.fullmatch(pattern, inp))
print(result)
