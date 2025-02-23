import re
txt_file = 'test.txt'
with open(txt_file, 'r') as file:
    textm = file.read()

inp = input()
result = re.sub(r'([a-z])([A-Z])', r'\1 \2', inp)
print(result)
