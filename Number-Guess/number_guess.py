import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

i = 0
while i == 0:
    guesses = 0
    diff = input("Choose a difficulty. Type 'easy' or 'hard: ")

    if diff == "easy":
        guesses = 10
        i = 1
    elif diff == "hard":
        guesses = 5
        i = 1
    else:
        print("Try again, you didn't choose 'easy' or 'hard'.")

secret_number = random.randint(1, 100)


def guess_calc():
    global secret_number
    if player_guess == 0:
        print("You lose, prick")
        exit()
    elif player_guess < secret_number:
        print("Too low! Try again")
        return guesses - 1
    elif player_guess > secret_number:
        print("Too high! Try again")
        return guesses - 1
    else:
        print("You win!")
        exit()


while guesses > 0:
    player_guess = input(f"You have {guesses} chances left, guess a number: ")
    player_guess = int(player_guess)
    guesses = guess_calc()
