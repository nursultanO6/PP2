stg = input()
pal = []
lap = []
if len(stg) % 2 == 0:
    for i in range(len(stg) // 2):
        pal.append(stg[i])
        lap.append(stg[i+(len(stg)//2)])
else:
    for i in range((len(stg) - 1) // 2):
        pal.append(stg[i])
        lap.append(stg[i+((len(stg) + 1)//2)])
if stg == ''.join(reversed(stg)):
    print("it is palindrome")
else:
    print("it is not palindrome")