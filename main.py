# Program for Valorant Competitive Parties
import random

#Collection of maps in lowercase
maps = ["bind", "haven", "split", "ascent", "icebox", "breeze", "fracture", "pearl", "lotus", "sunset", "abyss"]
#Collection of maps with first letter capitalize
maps_capitalize = [word.capitalize() for word in maps]

user_index = 0

def introduction_prompt():
    global user_index
    while user_index == 0:
        for i in maps_capitalize:
            print(f"{i}", end = " ")
        print()
        user_input = input("Select A Map (Q to Quit): ").lower()
        if user_input == "q":
            break
        elif user_input in maps:
            user_index = 1
            print(f"You've selected {user_input.capitalize()}.")
            site_selection_prompt(user_input)

def site_rolling(map_input):
    if map_input == "haven":
        no_of_sites = 3
    else:
        no_of_sites = 2
    random_site = random.randint(1, no_of_sites)
    match random_site:
        case 1:
            print("You've rolled for A site.")
        case 2:
            print("You've rolled for B site.")
        case 3:
            print("You've rolled for C site.")

def site_selection_prompt(map_input):
    user_input = input("Would you like to roll for site to attack? (Y/N): ")
    if user_input.lower() == "y":
        site_rolling(map_input)
    elif user_input.lower() == "n":
        print()#bring them back to introduction prompt
    else:
        print("Invalid input.")

def init():
    introduction_prompt()

init()