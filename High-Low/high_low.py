import random
from clear import clear

from high_low_data import data
from high_low_logo import logo, vs


choice_a = random.choice(data)
data.remove(choice_a)
choice_b = random.choice(data)
data.remove(choice_b)

lose = 0
check = 0
points = 0
i = 0
while i == 0 and points != 48:
    print(logo)
    print(f"You have {points} points.")
    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
    print(vs)
    print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if choice_a['follower_count'] > choice_b['follower_count']:
        if guess == "a":
            points += 1
            choice_b = random.choice(data)
            data.remove(choice_b)
        else:
            i += 1
            lose += 1
    elif choice_a['follower_count'] < choice_b['follower_count']:
        if guess == "b":
            points += 1
            choice_a = choice_b
            choice_b = random.choice(data)
            data.remove(choice_b)
        else:
            i += 1
            lose += 1
    else:
        i += 1
        check += 1
        lose += 1


if lose == 0:
    print("WOW YOU WIN!")
elif check == 1:
    print("You guessed something other than 'A' or 'B', and I'm too lazy to implement a workaround.")
    print("YOU LOSE!")
elif lose > 0:
    print(f"You got {points} points... surely you can do better.")
    print("YOU LOSE!")
