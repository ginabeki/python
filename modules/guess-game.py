from random import randint
import sys
# generate a number 1 -10
answer = randint(int(sys.argv[1]), int(sys.argv[2]))
# input from user?

# check that input is a number 1-10
while True:
    try:
        guess = int(input("guess a number 1-10: "))
        if guess > 0 and guess < 11:
            if guess == answer:
                print("You are a genius")
                break
        else:
            print("hey bozo, I said 1-10")
    except ValueError:
        print("please enter a number")
        continue
# check if number is right guess. Otherwise
# ask again

