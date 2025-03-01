strg = input()
sum = 0
for i in strg:
    if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
        sum += 1
print(sum)