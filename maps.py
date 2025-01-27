import random

def random_site(map_input):
    match map_input:
        case "haven":
            num_of_sites = 3
        case _:
            num_of_sites = 2
    roll = random.randint(1,num_of_sites)
    match roll:
        case 1:
            print("You've rolled for A site.")
        case 2:
            print("You've rolled for B site.")
        case 3:
            print("You've rolled for C site.")