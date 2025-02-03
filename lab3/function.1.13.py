import random
def takegues():
    name = input("Hello! What is your name?")
    sum = 0
    rand = random.randint(1, 20)
    print("Well, " + name + ", I am thinking of a number between 1 and 20.")
    while(True):
        print("take a guess")
        mynum = int(input())
        sum += 1
        if mynum == rand:
            print(f"Good job, {name}! You guessed my number in {sum} guesses!")
            break
        elif mynum > rand:
            print("Your guess is too high.")
        elif mynum < rand:
            print("Your guess is too low.")
takegues()
