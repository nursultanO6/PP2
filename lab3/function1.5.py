import itertools
strg = input()
per = itertools.permutations(strg)
for i in per:
    print(''.join(i))