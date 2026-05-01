import time

input("Welcome to Dungeon Exploration! Please click Enter to start the game")
time.sleep(1)
name = input("Welcome adventurer! Please enter your name: ")
time.sleep(1)
print("Welcome, " + name + "! You are about to begin this new adventure.")
time.sleep(1)
print("Your objective is to get the treasure. There are three ways to achieve this.")
time.sleep(1)

path = input("Choose your path (left/center/right): ")
time.sleep(1)

if path == "left":
    print("During your adventure in this silent cave you hear some steps. A wild ferocious orc appears!")
    time.sleep(2)
    strength = input("Choose your strength (1-5): ")
    if strength == "5":
        print("You demolished the orc! You gain the treasure!")
    elif strength == "4":
        print("Good hit! You defeated the enemy. You gain the treasure!")
    elif strength == "3":
        print("You almost survived! You still get the treasure!")
    else:
        print("Not enough strength! You have been slayed! Game over!")

elif path == "center":
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
    if answer == "footsteps":
        print("Correct! You still got one more riddle left")
    else:
        print("Wrong answer. You still got one more attempt")
    time.sleep(2)
    print("Riddle 2: What can fill a room but takes no space?")
    answer = input("Your answer: ")
    if answer == "light":
        print("Correct. The man nods. You may now gain access and collect the treasure")
    else:
        print("Wrong answer. I am afraid you are not worthy enough to get the treasure. Game over!")

elif path == "right":
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

time.sleep(2)
print("Thank you so much for playing this small game :)!")
input("Press Enter to exit...")
