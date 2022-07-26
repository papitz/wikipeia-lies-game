import random
import os

clear = lambda: os.system("clear")
clear()


# function to set words
def set_words(words):
    for user in words:
        if user == users[guessing_no]:
            continue
        clear()
        words[user] = input(f"Word for {user}: ")


# data structures
words = {}
number_of_users = int(input("How many users?\n"))
point_map = {}

# set uo users
for i in range(number_of_users):
    user = input(f"Name of user {i + 1}: ")
    words[user] = ""
    point_map[user] = 0

users = list(words.keys())

point_init = input("Initialize with points? (y/N)")
if point_init.lower() == "y":
    for user in point_map.keys():
        old_points = input(f"Points for {user}: ")
        point_map[user] = int(old_points)

# set up a user that guesses
guessing_no = 0
input(f"{users[guessing_no]} is guessing this round")

# set up words
set_words(words)

clear()

# game loop
while True:
    # guessing phase
    input("Press enter to get a random word...")
    possible_words = {}
    for name, word in words.items():
        if name == users[guessing_no]:
            continue
        possible_words[name] = word
    current_user, current_word = random.choice(list(possible_words.items()))
    print(f"Current Word: {current_word}")
    input("Press enter to reveal user...")
    print(current_user)

    # calculating points
    for i in range(len(users)):
        if i == guessing_no:
            continue
        print(f"{i + 1}. {users[i]}")
    winner = int(input("Number of user who won? ")) - 1
    if users[winner] == current_user:
        point_map[(users[guessing_no])] += 1
    point_map[(users[winner])] += 1

    # print points
    print("Points:")
    for user, points in point_map.items():
        print(f"{user}: {points}")

    input("Press enter for new round...")

    # set a new person who is guessing
    guessing_no = (guessing_no + 1) % number_of_users
    input(f"{users[guessing_no]} is guessing this round")

    # get new words
    set_words(words)

    clear()
