import os
cf = r"C:\Users\Nursultan\Desktop\projects\PP2\lab6\A.txt"
path = os.getcwd()
if os.access(cf, os.F_OK) == True:
    os.rmdir(cf)
else:
    print('File doesnt exist')