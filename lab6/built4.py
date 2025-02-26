import time
import math
num = int(input())
milli = int(input())
res = math.sqrt(num)
time.sleep(milli/1000)
print(f"Square root of {num} after {milli} miliseconds is {res}")