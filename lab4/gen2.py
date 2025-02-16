n = int(input("Enter: "))
for i in range(n+1):
    if(i%2 == 0):
        print(i,end="")
    else:
        print(',',end="")