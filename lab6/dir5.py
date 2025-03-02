listt = ["apple", "banana", "cherry", "date"]

with open("tests.txt", "w") as file:
    for i in listt:
        file.write(i + " ")
