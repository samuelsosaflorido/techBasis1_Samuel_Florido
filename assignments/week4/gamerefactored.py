# Dungeon Exploration. A text adventure game inspired in classic RPG format
# The main objective of this game is that the player needs to make decisions through different routes in order to find and gain a treasure. Will the player survive? Will the player be worthy enough? 

import time

# Constants
GAME_TITLE = "Dungeon Exploration"
RIDDLE1_ANSWER = "footsteps"
RIDDLE2_ANSWER = "light"
WINNING_MESSAGE = "You gain the treasure!"
LOSING_MESSAGE = "Game over!"
DIRECTIONS = ["left", "center", "right"]


def introduction():
    input("Welcome to Dungeon Exploration! Please click Enter to start the game")
    time.sleep(1)
    name = input("Welcome adventurer! Please enter your name: ")
    time.sleep(1)
    print("Welcome, " + name + "! You are about to begin this new adventure.")
    time.sleep(1)
    print("Your objective is to get the treasure. There are three ways to achieve this.")
    time.sleep(1)
    return name


def check_strength(strength):
    # Strenght is being added as an argument and takes the result from the different choices 
    if strength == "5":
        return "You demolished the orc! " + WINNING_MESSAGE
    elif strength == "4":
        return "Good hit! You defeated the enemy! " + WINNING_MESSAGE
    elif strength == "3":
        return "You almost survived! " + WINNING_MESSAGE
    else:
        return "Not enough strength! You have been slayed! " + LOSING_MESSAGE


def orc_battle():
    # In the left path the player encounters a wild orc
    print("During your adventure in this silent cave you hear some steps. A wild ferocious orc appears!")
    time.sleep(2)
    strength = input("Choose your strength (1-5): ")
    result = check_strength(strength)
    print(result)


def hooded_man():
    # The center path will have a mysterious hooded man that will give the player two riddles 
    print("You enter in a strange area with a strange hooded man")
    time.sleep(2)
    print("His appearance makes you feel strange")
    time.sleep(2)
    print("You can barely see his face")
    time.sleep(2)
    print("He is completely covered by a massive hood and holds an ancient staff")
    time.sleep(2)
    print("The man suddenly speaks")
    time.sleep(2)
    print("You feel a strange shiver")
    time.sleep(2)
    print("He says: In order to access the treasure of this dungeon you need to solve two riddles")
    time.sleep(2)
    print("Riddle 1: The more you take, the more you leave behind. What am I?")
    time.sleep(2)
    answer = input("Your answer: ")
    if answer == RIDDLE1_ANSWER:
        print("Correct! You still got one more riddle left")
    else:
        print("Wrong answer. You still got one more attempt")
    time.sleep(2)
    print("Riddle 2: What can fill a room but takes no space?")
    answer = input("Your answer: ")
    if answer == RIDDLE2_ANSWER:
        print("Correct. The man nods. You may now gain access and collect the treasure")
    else:
        print("Wrong answer. I am afraid you are not worthy enough to get the treasure. Game over!")


def dragon_stealth():
    # In the right path section, the player will encounter a dragon and will have to sneak through this section in order to get the treasure 
    print("This route leads to a vast area in which....there is a dragon sleeping!")
    time.sleep(2)
    stealth = input("How sneaky are you going to move? (1-5): ")
    if stealth == "5":
        print("You sneaked past the dragon! You get the treasure!")
    elif stealth == "4":
        print("You go through without much noise. You get the treasure!")
    elif stealth == "3":
        print("You make some noise but the dragon doesn't wake up. You get the treasure!")
    else:
        print("The dragon awakens. Game over!")


def main():
    name = introduction()
    path = input("Choose your path (left/center/right): ")
    time.sleep(1)
    if path == "left":
        orc_battle()
    elif path == "center":
        hooded_man()
    elif path == "right":
        dragon_stealth()
    time.sleep(2)
    print("Thank you so much for playing this small game :)!")
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
