def div(a):
    for i in range(a, -1, -1):
        yield i
    
a = int(input("Enter: "))

for num in div(a):
    print(num)