import os
copyf = r"C:\Users\Nursultan\Desktop\projects\PP2\test.txt"
copiedf = r"C:\Users\Nursultan\Desktop\projects\PP2\lab6\A.txt"
try:
    with open(copyf, 'r') as src, open(copiedf, 'w') as dest:
        content = src.read()
        dest.write(content)
except Exception as e:
    print(f"An error occurred: {e}")