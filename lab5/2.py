import re
txt_file = 'test.txt'
with open(txt_file, 'r') as file:
    textm = file.read()

inp = input()
pattern = r'^ab{2,3}$'
result = bool(re.fullmatch(pattern, inp))
print(result)