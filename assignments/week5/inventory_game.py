# Memories. A small psychological horror experience

import time

# Inventory management

MAX_INVENTORY = 5

inventory = []

items_in_room = [
    {
        "name": "note",
        "type": "clue",
        "uses": 1,
        "description": "It is a handwritten note. There's a love confession on it. You feel the need to cry but you do not know why. You feel something in your heart that you cannot fully understand"
    },
    {
        "name": "newspaper",
        "type": "clue",
        "uses": 1,
        "description": "This is a newspaper from two weeks ago. Some of its pages are covered by blood. You can identify that a group research from the hospital have been under detention and punished. You see some pictures. You start recognizing all of them."
    },
    {
        "name": "journal",
        "type": "clue",
        "uses": 1,
        "description": "A research journal from the lab team. Subject: XL34. You read the entire of it and something makes you feel strange. The last two lines says the following: 'We may have gone too far. May god be merciful and forgive us'"
    },
    {
        "name": "photo",
        "type": "clue",
        "uses": 1,
        "description": "A photograph. You start to shiver. You recognize yourself in the photo. Surrounded by familiar people. A woman, two children...Everyone is smiling. You are not. You start sobbing but you control yourself"
    },
    {
        "name": "keycard",
        "type": "clue",
        "uses": 1,
        "description": "An ID card with your name. Under ROLE it says: XL34. Under STATUS: Subject of experimentation. DO NOT RELEASE UNDER ANY CIRCUMSTANCES."
    }
]

key_found = False
examined = []
game_ended = False


# ---------- Functions ----------

def show_inventory():
    if not inventory:
        print("Your pockets are empty.")
        return

    print(f"\nInventory ({len(inventory)}/{MAX_INVENTORY}):")

    for item in inventory:
        print("- " + item["name"])


def show_room_items():
    print("\nYou look around the room.")

    time.sleep(2)

    print(
        "White walls. All feels the same. Boring, claustrophobic. A strange ominous door at the end."
    )

    time.sleep(2)

    print("You notice:")

    for item in items_in_room:
        print(" - " + item["name"])

    if key_found:
        print(" - key")


def pick_up(item_name):
    for item in items_in_room:

        if item["name"] == item_name:

            if len(inventory) >= MAX_INVENTORY:
                print("You can't carry more items. Drop something first.")
                return

            inventory.append(item)
            items_in_room.remove(item)

            print(f"You pick up the {item['name']}.")

            return

    print(f"There is no '{item_name}' here.")


def drop(item_name):
    for item in inventory:

        if item["name"] == item_name:
            inventory.remove(item)
            items_in_room.append(item)

            print(f"You drop the {item['name']}.")

            return

    print(f"You don't have '{item_name}'.")


def use(item_name):
    for item in inventory:

        if item["name"] == item_name:

            if item["name"] == "note":

                print("You flip the note over.")

                time.sleep(2)

                print("There's nothing.")

                time.sleep(2)

                print("You start examining the object from the other side.")

                time.sleep(2)
                print("What is all this? I need answers...why I am here. What is this...oh no")

            elif item["name"] == "newspaper":

                print("You open the newspaper.")

                time.sleep(2)

                print("You start examining the object.")

                time.sleep(2)

                print("You start feeling dazed and confused.")

            elif item["name"] == "journal":

                print("You open the journal.")

                time.sleep(2)

                print("What you see is extremely painful. You feel a strong headache and start feeling nervous")

                time.sleep(2)

                print(
                    "You feel the need to read more but you the fear is growing stronger. It is something very deep that you cannot explain")

            elif item["name"] == "photo":

                print("You bring the photo closer to your face.")

                time.sleep(2)

                print("The faces are familiar. Too familiar.")

                time.sleep(2)

                print("You feel your heart breaking and start shaking")

            elif item["name"] == "keycard":

                print("You watch the keycard closely.")

                time.sleep(2)

                print("You start examining the object.")

                time.sleep(2)

                print("Everything feels more confusing. You need to remember what happened.")

            elif item["name"] == "key":

                ending()

            else:

                print("Nothing happens.")

            return

    print(f"You don't have '{item_name}'.")


def examine(item_name):
    global key_found

    for item in inventory + items_in_room:

        if item["name"] == item_name:

            print(f"\n{item['description']}")

            time.sleep(3)

            if item["name"] == "note":

                print(
                    "Then a voice suddenly appears. You hear it in every part of your body. You scream. Nobody hears you."
                )

                time.sleep(3)

                print("You cannot escape the truth'")

                time.sleep(3)
                print("What is that? Am I going insane? What is going on? What are you? Show yourself!")

                time.sleep(3)
                print("You receive no answer")

            elif item["name"] == "newspaper":

                time.sleep(3)

                print("You start reading it. You still feel confused")

                time.sleep(3)

                print("What is this? Why is this here? What am I doing here?")

                time.sleep(3)

                print("The voice again appears: 'Who are you? What are you?'")

                print("Enough of this! Reveal yourself! What is going on here?!")

                time.sleep(3)
                print("Again no answer")

                time.sleep(3)
                print("Am I going insane? Is this happening inside my head?")

            elif item["name"] == "journal":

                time.sleep(3)

                print("The experiment is well-detailed. You start realizing the horror behind all this...")

                time.sleep(3)

                print("Pay the consequences of your actions.'")

                time.sleep(3)
                print("What...Oh no...what is going on here? No..")

            elif item["name"] == "photo":

                time.sleep(2)

                print("Memories start to appear.")

                time.sleep(2)

                print("The voice: 'Do you remember their names? Of course you do. You still love them'")

                time.sleep(2)

                print(
                    "My head...I cannot handle this is too much. I do remember their laughs. I do remember them but why?")

                time.sleep(2)

                print("You start to feel a sense of dread like never before.")

            elif item["name"] == "keycard":

                time.sleep(3)

                print("Your hands are shaking while holding the keycard.")

                time.sleep(3)

                print("No! This cannot be me! This is not me!")

                time.sleep(3)

                print("The voice says: 'You are a monster. You do not deserve to live'")

                time.sleep(3)

                print("Then you all of sudden receive a huge impact within your mind. You cannot hold it anymore")

                time.sleep(3)
                print("You fell on your knees and start crying and screaming")

                time.sleep(3)

                print("You then realize what happened")
                time.sleep(3)

                print("I deserve to die. I deserve to be punished. I am so sorry....")

                time.sleep(3)

                if not key_found:
                    key_found = True

                    key_item = {
                        "name": "key",
                        "type": "key",
                        "description": "A small cold key. It feels like it has been waiting for you."
                    }

                    items_in_room.append(key_item)

                    print("\nSomething falls from behind the keycard. A key.")
                    print("Type 'pickup key' and then 'use key'.")

            return

    print(f"You don't see '{item_name}' here or in your pockets.")


def ending():
    global game_ended

    print("\nYou walk to the door.")

    time.sleep(2)

    print("You insert the key.")

    time.sleep(2)

    print("The lock turns.")

    time.sleep(2)

    print("The door opens.")

    time.sleep(2)

    print("Beyond it you see a strong light but you cannot see what's beyond it.")

    time.sleep(2)

    print("\nThe voice laughs. Slowly. Quietly.")

    time.sleep(3)

    print("'You are a monster. You cannot escape the past'")

    time.sleep(3)

    print("True...I am a monster. I do not deserve to live but...maybe there's a chance to redeem myself?")

    time.sleep(3)

    print("The voice does not say anything but you know it's still there.")

    time.sleep(3)

    print("Will I be able to release my pain? Will I be able to forgive myself?.")

    time.sleep(3)

    print("The voice does not say anything but you get the feeling that whatever is watching you is smiling")

    time.sleep(3)

    print("\n" + "=" * 40)

    print("   MEMORIES.")

    print("   YOU ESCAPED.")

    print("   OR DID YOU?")

    print("=" * 40)

    input("\nPress Enter to exit")

    game_ended = True


# ---------- GAME LOOP ----------

def game_loop():
    print("\n" + "=" * 40)
    print("   Memories: A psychological horror experience")
    print("=" * 40)

    time.sleep(2)

    print("\nYou wake up in a strange room.")

    time.sleep(2)

    print("It looks like a normal hospital room. But something is off.")

    time.sleep(2)

    print("You barely remember who you are or who you were.")

    time.sleep(2)

    print("You have the feeling that someone or something is watching you.")

    time.sleep(2)

    print("You need to escape.")

    time.sleep(2)

    print("\nType 'help' for commands. Type 'look' to start.\n")

    while not game_ended:

        command = input("\n> ").strip().lower()

        match command.split():

            case ["help"]:
                print("Commands: look, inventory, pickup [item], drop [item], use [item], examine [item], quit")

            case ["look"]:
                show_room_items()

            case ["inventory"]:
                show_inventory()

            case ["pickup", item_name]:
                pick_up(item_name)

            case ["drop", item_name]:
                drop(item_name)

            case ["use", item_name]:
                use(item_name)

            case ["examine", item_name]:
                examine(item_name)

            case ["quit"]:
                print("You close your eyes.")
                break

            case _:
                print("Unknown command. Type 'help' to see available commands.")


if __name__ == "__main__":
    game_loop()
