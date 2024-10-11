import random
play=True
number=str(random.randint(1,10))
guess=input("Guess a number between 1 and 10: ")
if number==guess:
    print("You win")
else:
    print("You lose, number is", number)