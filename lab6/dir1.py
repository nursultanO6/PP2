import os
path = 'C:\Program Files (x86)\epson\Epson Scan 2\Drivers\ES022B'

result = os.listdir(path)
for i in result:
    print(i)