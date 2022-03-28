# import random
# game = ['Rock', 'Paper', 'Scissors']
# print(f"Select any option from {game}. \nWe hope it doesn't end in tears.")
# com_choice = random.choice(game)
# random.shuffle(game)
# print("Pick a choice:")
# user_choice = str(input(">"))

# if user_choice == com_choice:
#     print(f"Both players selected {user_choice}. It's a tie!")
# elif user_choice == "Rock":
#     if com_choice == "Scissors":
#         print("You win!")
#     else:
#         print("You lose.")
# elif user_choice == "Paper":
#     if com_choice == "Rock":
#         print("You win!")
#     else:
#         print("You lose.")
# elif user_choice == "Scissors":
#     if com_choice == "Paper":
#         print("You win!")
#     else:
#         print("You lose.")

# import random

# choices = ['r', 'p', 's']

# def check_winner(player_choice, com_choice):
#     if player_choice == "r" and com_choice== "s":
#         return "Player Wins"
#     elif player_choice == "p" and com_choice== "r":
#         return "Player Wins"
#     elif player_choice == "s" and com_choice =="p":
#         return "Player Wins"
#     if player_choice == "s" and com_choice== "r":
#         return "Player Wins"
#     elif player_choice == "r" and com_choice== "p":
#         return "Player Wins"
#     elif player_choice == "p" and com_choice =="s":
#         return "Player Wins"
#     else:
#         return "It's a tie"


# print("Welcome to rock paper scissors.\nEnter R for Rock, P for Paper, S for Scissors.")


# player_choice = input(">").lower()
# com_choice = random.choice(choices)
# if player_choice in choices:
#     result = check_winner(player_choice, com_choice)


#     print(result)
#     print(f"Cmputer selected {com_choice}")
# else:
#     print("Invalid input")

h = 0

# while h <= 10:
#     if h ==10:
#         print("BOOM")
#     else:
#         print(h)
    
#     h+=1

import random
a = [3,2,5,6,8,7]
def game():
    print(f"Select any number from {a}. \nWe hope it doesn't end in tears.")
    com_choice = random.choice(a)
    random.shuffle(a)
    print("Guess the number:")
    user_choice = int(input(">"))

    if user_choice in a:
        if user_choice == com_choice:
            print("All power belongs to you, comrade.")
        else:
                print("Arrhh,comrade. Be like you go try again")
    else:
            print("Comrade, nor be so!")

i = 1
while True:

    game()
    c = input("Continue?\n>")
    if c == "y":
        continue
    else:
        break


