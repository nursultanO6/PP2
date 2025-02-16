def div(a, b):
    for i in range(a,b + 1):
        yield i*i
    
a = int(input("Enter: "))
b = int(input("Enter: "))

for num in div(a, b):
    print(num)