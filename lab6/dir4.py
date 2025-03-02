file_name = r"C:\Users\Nursultan\Desktop\projects\PP2\test.txt"  

with open(file_name, 'r') as file:
    summ = sum(1 for i in file)

print(f"Number of lines: {summ}")