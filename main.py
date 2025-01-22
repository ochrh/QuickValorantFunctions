# Program for Valorant Competitive Parties

import random

#Date of Release
maps = {"Bind", "Haven", "Split", "Ascent", "Icebox", "Breeze", "Fracture", "Pearl", "Lotus", "Sunset", "Abyss"}
userSelected = False
sites = 2

def translate_site(fSiteInt):
    siteAlphabet = ""
    if fSiteInt == 1:
        siteAlphabet = "A"
    elif  fSiteInt == 2:
        siteAlphabet = "B"
    elif fSiteInt == 3:
        siteAlphabet = "C"
    return siteAlphabet


def roll_attack_site(fMapChoice, fMapSites):
    if fMapChoice == "haven": fMapSites = 3
    print("Tough time deciding which site to attack? ")
    rollOption = str(input(f"Roll for attack side for {fMapChoice.capitalize()} (Y or N):"))
    if rollOption.lower() == "n":
        print("Quit")
    elif rollOption.lower() == "y":
        randomSite = random.randint(1,fMapSites)
        print(translate_site(randomSite))


for i in maps:
    print(f"{i}", end = " ")
print()

while not userSelected:
    userOption = input("Select A Map (Q to Quit): ").lower()
    if userOption == "q":
        break
    else:
        for i in maps:
            optionCheck = i.lower()
            if userOption == optionCheck:
                userSelected = True
                print(f"You've selected {userOption.capitalize()}.")
                roll_attack_site(userOption,sites)