
import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
player_pick_one = random.choice(cards)
player_pick_two = random.choice(cards)
computer_pick_one = random.choice(cards)
computer_pick_two = random.choice(cards)

count_player = player_pick_one + player_pick_two
count_computer = computer_pick_one + computer_pick_two

print("Your cards: " + f'{player_pick_one}' + ", " + f'{player_pick_two}')
print("Computer shown card: " + f'{computer_pick_one}')

def compute():
    if count_player > count_computer & count_computer < 22:
        print("Your total is: " + f'{count_player}')
        print("Computer total is: " + f'{count_computer}')
        print("You win!")
    elif count_player < count_computer & count_computer < 22:
        print("Your total is: " + f'{count_player}')
        print("Computer total is: " + f'{count_computer}')
        print("You suck!")
    elif count_player == count_computer & count_computer < 22:
        print("Your total is: " + f'{count_player}')
        print("Computer total is: " + f'{count_computer}')
        print("Drawing is just as bad as losing")
    else:
        print("Your total is: " + f'{count_player}')
        print("Computer total is: " + f'{count_computer}')
        print("You win!")

choose = input("Would you like to hit or stay?")
if choose == "hit":
    player_pick_three = random.choice(cards)
    print("Your cards: " + f'{player_pick_one}' + ", " + f'{player_pick_two}' + ", " + f'{player_pick_three}')
    count_player += player_pick_three
    if count_player > 21:
        print("Your total is: " + f'{count_player}')
        print("You suck!")
        exit()
elif choose == "stay":
    if count_computer < 17:
        computer_pick_three = random.choice(cards)
        count_computer += computer_pick_three
    if count_computer < 17:
        computer_pick_four = random.choice(cards)
        count_computer += computer_pick_four
    if count_computer < 17:
        computer_pick_five = random.choice(cards)
        count_computer += computer_pick_five
    compute()
    exit()

choose2 = input("Would you like to hit or stay?")
if choose2 == "hit":
    player_pick_four = random.choice(cards)
    print("Your cards: " + f'{player_pick_one}' + ", " + f'{player_pick_two}' + ", " + f'{player_pick_three}' + ", " + f'{player_pick_four}')
    count_player += player_pick_four
    if count_player > 21:
        print("Your total is: " + f'{count_player}')
        print("You suck!")
        exit()
elif choose2 == "stay":
    if count_computer < 17:
        computer_pick_three = random.choice(cards)
        count_computer += computer_pick_three
    if count_computer < 17:
        computer_pick_four = random.choice(cards)
        count_computer += computer_pick_four
    if count_computer < 17:
        computer_pick_five = random.choice(cards)
        count_computer += computer_pick_five
    compute()
    exit()

choose3 = input("Would you like to hit or stay?")
if choose3 == "hit":
    player_pick_five = random.choice(cards)
    print("Your cards: " + f'{player_pick_one}' + ", " + f'{player_pick_two}' + ", " + f'{player_pick_three}' + ", " + f'{player_pick_four}' + ", " + f'{player_pick_five}')
    count_player += player_pick_five
    if count_player > 21:
        print("Your total is: " + f'{count_player}')
        print("You suck!")
        exit()
elif choose3 == "stay":
    if count_computer < 17:
        computer_pick_three = random.choice(cards)
        count_computer += computer_pick_three
    if count_computer < 17:
        computer_pick_four = random.choice(cards)
        count_computer += computer_pick_four
    if count_computer < 17:
        computer_pick_five = random.choice(cards)
        count_computer += computer_pick_five
    compute()
    exit()

if count_player <= 21:
    print("You Win!")
else:
    print("You suck!")

