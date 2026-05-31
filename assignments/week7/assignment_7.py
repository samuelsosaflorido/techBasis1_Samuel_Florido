# Comment on the code: 
# In order to begin with, I have realized that I have been posting all the information of my previous assignments on the ReadMe and it is preferable to explain the code within the code. 
# The design ideas are completely mine but in order to write, implement and understand the code I used Claude AI as it allowed me to get a better perspective and to receive feedback. Nevertheless, the changes and concepts are strictly personal and the use of AI allowed me to work through this. 
# For this assignment, I took my previous RPG game as it offered me new layers in terms of adding new systems. This is particularly notorious in the left path where I decided to expand the area, adding new layers for the combat system, adding lifepoints, health system, better time loops for the player to engage and also allowed the enemies to counterattack. 
# Furthermore, I decided to add new enemies: an undead creature, an unholy demon (which is kinda redundant, I know) and the Necromancer Lord, the final boss. For the last enemy I had a lot of problems and had to test it out several times and corrected the mistakes in terms of difficulty, as it was unfair and made no sense. 
# Adding these new layers for the game ended up being extremely interesting and I believe this has improved my game quite a lot. 
# I added new constants according to the new changes within the combat system with the corresponing health of the enemies, the damage and the structure of the records file for the player to see its progress and save it
# Afterwards, I added the functions in order to define the folders and export them in the CSV format.
# The datetime.now() allows the game to capture the exact moment in which the player manages to complete the game with its results
# the row = [name, timestamp, score, outcome] creates this list that will allow to save this information in the CSV file
# The rest of the code checks whether the file exists, writes the data and transforms the list into a dictionary, also using Claude I added the except OSError in case there are mistakes in terms of showing this information or to fix any problem that might appear 
# The function relative to the records basically gives structure to this list and filters if there is also any possible corrupted score 
# The rest of the code has been modified in order to add these scores. The major change has been introduced in the left path as mentioned before. Since I decided to expand this area, I changed the name to fight_enemy as the player will have to face numerous waves in order to gain the treasure
# Adding the "while player_hp > 0 and enemy_hp > 0: makes the system function and allows the player to engage with a much more dynamic combat system than the previous version and also gives this sense of reward at the end 
# I added all these changes as well to the main function so the program can register this and work with the new changes. 
# For the center route, using the support of Claude, I added "score = 100 if won else 0" and "outcome = "Win" if won else "Loss"" in a much more engaging way to register the conditional statements of if/else 
# For the riddles function I added either True or False, like in the refractored version that we practised in the week4/5
# For the dragon_stealth function, I also added something similar but with a score map in order to get the results. The more stealthy you move through this section, the better and will also allow the player to get better results at the end of the game. 
# Finally, for the main function, adding the DEBUG mode either to True or False will either skip the game to see the results or test it, being this last one the default mode. 


import time
import csv
import os
from datetime import datetime

# Debug
DEBUG = False

# Constants
GAME_TITLE = "Dungeon Exploration"
RIDDLE1_ANSWER = "footsteps"
RIDDLE2_ANSWER = "light"
WINNING_MESSAGE = "You gain the treasure!"
LOSING_MESSAGE = "Game over!"
DIRECTIONS = ["left", "center", "right"]
DEBUG_PLACEHOLDER_SCORE = 0
STRENGTH_DAMAGE = {"5": 80, "4": 60, "3": 40, "2": 20, "1": 10}
ORC_HP = 60
UNDEAD_HP = 50
DEMON_HP = 100
BOSS_HP = 400
ORC_DAMAGE = 15
UNDEAD_DAMAGE = 20
DEMON_DAMAGE = 30
BOSS_DAMAGE = 45
RECORDS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "records.csv")
CSV_HEADERS = ["Name", "Timestamp", "Score", "Outcome"]


# Records

def save_record(name, score, outcome):
    """Save a single game result to the CSV file."""
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    row = [name, timestamp, score, outcome]
    try:
        file_exists = os.path.isfile(RECORDS_FILE)
        with open(RECORDS_FILE, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            if not file_exists:
                writer.writerow(CSV_HEADERS)
            writer.writerow(row)
            print("\nRecord saved successfully!")
    except OSError as e:
        print(f"\nCould not save record: {e}")


def load_records():
    """Load all records from the CSV file. Returns a list of dicts."""
    try:
        with open(RECORDS_FILE, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            records = list(reader)
        return records
    except FileNotFoundError:
        return []
    except OSError as e:
        print(f"\nCould not load records: {e}")
        return []


def display_leaderboard():
    """Display the top-10 leaderboard sorted by score descending."""
    records = load_records()
    if not records:
        print("\nNo previous records found.")
        return
    try:
        sorted_records = sorted(
            records,
            key=lambda r: int(r["Score"]),
            reverse=True
        )
    except (KeyError, ValueError) as e:
        print(f"\nCould not sort records: {e}")
        sorted_records = records

    top10 = sorted_records[:10]
    print("\n" + "=" * 55)
    print(f"{'LEADERBOARD':^55}")
    print("=" * 55)
    print(f"{'#':<4}{'Name':<18}{'Score':<8}{'Outcome':<15}{'Date'}")
    print("-" * 55)
    for i, rec in enumerate(top10, 1):
        print(
            f"{i:<4}{rec['Name']:<18}{rec['Score']:<8}"
            f"{rec['Outcome']:<15}{rec['Timestamp']}"
        )
    print("=" * 55)


# Game Mechanic and Logic

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


def fight_enemy(enemy_name, player_hp, enemy_hp, enemy_damage):
    # Turn-based combat with counterattack and heal option
    print(f"\nAn {enemy_name} appears!")
    time.sleep(1)

    while player_hp > 0 and enemy_hp > 0:
        print(f"\nYour HP: {player_hp} | {enemy_name.capitalize()} HP: {enemy_hp}")
        time.sleep(1)
        action = input("What do you do? (attack/heal): ").strip().lower()

        if action == "heal":
            player_hp += 100
            print(f"You drink a potion. HP restored to {player_hp}")
            time.sleep(1)
        elif action == "attack":
            strength = input("Choose your strength (1-5): ").strip()
            damage = STRENGTH_DAMAGE.get(strength, 0)
            enemy_hp -= damage
            print(f"You deal {damage} damage! {enemy_name.capitalize()} HP: {enemy_hp}")
            time.sleep(1)

        if enemy_hp > 0:
            player_hp -= enemy_damage
            print(f"The {enemy_name} strikes back! You take {enemy_damage} damage. Your HP: {player_hp}")
            time.sleep(1)

    if enemy_hp <= 0:
        print(f"You defeated the {enemy_name}!")
    else:
        print(f"The {enemy_name} kills you. " + LOSING_MESSAGE)

    return player_hp


def final_boss(hp):
    # Multiturn boss fight against the Necromancer Lord
    boss_hp = BOSS_HP
    time.sleep(2)

    while hp > 0 and boss_hp > 0:
        print(f"\nYour HP: {hp} | Boss HP: {boss_hp}")
        time.sleep(1)
        action = input("What do you do? (attack/heal): ").strip().lower()

        if action == "heal":
            hp += 100
            print(f"You drink a potion. HP restored to {hp}")
            time.sleep(1)
        elif action == "attack":
            strength = input("Choose your attack strength (1-5): ").strip()
            damage = STRENGTH_DAMAGE.get(strength, 0)
            boss_hp -= damage
            print(f"You deal {damage} damage! Boss HP: {boss_hp}")
            time.sleep(1)

        if boss_hp > 0:
            hp -= BOSS_DAMAGE
            print(f"The Necromancer strikes back! You take {BOSS_DAMAGE} damage. Your HP: {hp}")
            time.sleep(1)

    if boss_hp <= 0:
        print("You have defeated the Necromancer Lord! " + WINNING_MESSAGE)
        return hp, "Win"
    else:
        print("You feel your life being drained away. The Necromancer Lord absorbs your soul. " + LOSING_MESSAGE)
        return 0, "Loss"


def left_path():
    # The left path presents several encounters that the player needs to face. It is divided in four sections:
    hp = 300

    # First section: wild orc
    print("During your adventure in this silent cave you hear some steps")
    time.sleep(2)
    hp = fight_enemy("orc", hp, ORC_HP, ORC_DAMAGE)
    if hp <= 0:
        return 0, "Loss"

    # Second section: undead enemy
    print("You continue your adventure within this cave. You hear some strange sounds")
    time.sleep(2)
    hp = fight_enemy("undead", hp, UNDEAD_HP, UNDEAD_DAMAGE)
    if hp <= 0:
        return 0, "Loss"

    # Third section: demon
    print("You manage to go to a large area within the cave. You hear some wild growls")
    time.sleep(2)
    hp = fight_enemy("unholy demon", hp, DEMON_HP, DEMON_DAMAGE)
    if hp <= 0:
        return 0, "Loss"

    # Fourth section: Final boss
    print("At the end of the cave you see the treasure. You try to get it but something forbids you to access it")
    time.sleep(2)
    print("Some powerful spell")
    time.sleep(2)
    print("You then realize that there is a large figure holding a powerful sword, amulets and a skull staff")
    time.sleep(2)
    print("You then say: Alright, my final act in this Quest. Let the Gods decide my fate!")
    time.sleep(2)
    score, outcome = final_boss(hp)
    return score, outcome


def check_stealth(stealth):
    # Takes stealth as argument and returns the result message
    if stealth == "5":
        return "You sneaked past the dragon! " + WINNING_MESSAGE, True
    elif stealth == "4":
        return "You go through without much noise. " + WINNING_MESSAGE, True
    elif stealth == "3":
        return "You make some noise but the dragon doesn't wake up. " + WINNING_MESSAGE, True
    else:
        return "The dragon awakens. " + LOSING_MESSAGE, False


def check_riddles(answer1, answer2):
    # Takes both answers as arguments and returns the result message
    if answer1 == RIDDLE1_ANSWER and answer2 == RIDDLE2_ANSWER:
        return "Correct. The man nods. You may now collect the treasure. " + WINNING_MESSAGE, True
    else:
        return "Wrong answer. I am afraid you are not worthy to collect the treasure. " + LOSING_MESSAGE, False
  
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
    answer1 = input("Your answer: ").strip().lower()
    answer2 = ""
    if answer1 == RIDDLE1_ANSWER:
        print("Correct! You still got one more riddle left")
        time.sleep(2)
        print("Riddle 2: What can fill a room but takes no space?")
        time.sleep(2)
        answer2 = input("Your answer: ").strip().lower()
    else:
        print("Wrong answer. " + LOSING_MESSAGE)
        return 0, "Loss"
    result, won = check_riddles(answer1, answer2)
    print(result)
    score = 100 if won else 0
    outcome = "Win" if won else "Loss"
    return score, outcome

def dragon_stealth():
    # In the right path section, the player will encounter a dragon and will have to sneak through in order to get the treasure
    print("This route leads to a vast area in which....there is a dragon sleeping!")
    time.sleep(2)
    stealth = input("How sneaky are you going to move? (1-5): ").strip()
    result, won = check_stealth(stealth)
    print(result)
    score_map = {"5": 100, "4": 75, "3": 50}
    score = score_map.get(stealth, 0)
    outcome = "Win" if won else "Loss"
    return score, outcome


def main():
    if DEBUG:
        print("DEBUG MODE - skipping main game loop.\n")
        name = input("Enter your name (debug): ").strip() or "Tester"
        score = DEBUG_PLACEHOLDER_SCORE
        outcome = "Debug"
    else:
        name = introduction()
        path = input("Choose your path (left/center/right): ").strip().lower()
        time.sleep(1)

        if path == "left":
            score, outcome = left_path()
        elif path == "center":
            score, outcome = hooded_man()
        elif path == "right":
            score, outcome = dragon_stealth()
        else:
            print("Invalid path chosen. Game over!")
            score, outcome = 0, "Loss"

        time.sleep(2)
        print("\nThank you so much for playing this small game :)!")

    save_record(name, score, outcome)
    display_leaderboard()

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
