import random

winningNumber = random(1,100)
guess = 1

number = int(input("Guess the numbeer : "))

game_over = False

while not game_over:
    if(number == winningNumber):
        print(f"You Win  in {guess} times")
        game_over = True

    else:
        if(number < winningNumber):
            print("Low guess ")
        else:
            print("Hogh huess")
