import re
txt_file = 'test.txt'
with open(txt_file, 'r') as file:
    textm = file.read()

inp = input()
result = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), inp)
print(result)
