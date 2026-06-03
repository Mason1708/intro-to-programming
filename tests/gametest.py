# Variables
has_sword = False
has_key = False
has_treasure = False

def start_game():
    print("\n=== THE LOST CRYSTAL ===")
    print("The Crystal of Light has been stolen!")
    print("1. Go to the forest")
    print("2. Go to the village")

    choice = input("> ")

    if choice == "1":
        forest()
    elif choice == "2":
        village()
    else:
        start_game()

def forest():
    global has_sword

    print("\nYou enter the Whispering Forest.")
    print("1. Follow the path")
    print("2. Search the campsite")

    choice = input("> ")

    if choice == "1":
        wolf_encounter()
    elif choice == "2":
        print("You found an ancient sword!")
        has_sword = True
        wolf_encounter()
    else:
        forest()

def wolf_encounter():
    print("\nA giant wolf blocks your path.")
    print("1. Fight")
    print("2. Run")

    choice = input("> ")

    if choice == "1":
        if has_sword:
            print("You defeat the wolf!")
            mountain()
        else:
            game_over()
    elif choice == "2":
        village()
    else:
        wolf_encounter()

def village():
    print("\nYou arrive at the village.")
    print("1. Visit the blacksmith")
    print("2. Talk to the old traveler")

    choice = input("> ")

    if choice == "1":
        blacksmith()
    elif choice == "2":
        traveler()
    else:
        village()

def blacksmith():
    print("\nThe blacksmith repairs your equipment.")
    mountain()

def traveler():
    print("\nThe traveler tells you about a hidden cave.")
    mountain()

def mountain():
    global has_key

    print("\nYou reach the mountains.")
    print("1. Cross the bridge")
    print("2. Search the eagle nest")

    choice = input("> ")

    if choice == "1":
        cave_entrance()
    elif choice == "2":
        print("You found a key!")
        has_key = True
        cave_entrance()
    else:
        mountain()

def cave_entrance():
    print("\nYou discover a cave behind a waterfall.")
    print("1. Enter")
    print("2. Turn back")

    choice = input("> ")

    if choice == "1":
        dragon_encounter()
    elif choice == "2":
        village()
    else:
        cave_entrance()

def dragon_encounter():
    print("\nA dragon guards the crystal.")
    print("1. Fight")
    print("2. Negotiate")

    choice = input("> ")

    if choice == "1":
        if has_sword:
            final_choice()
        else:
            game_over()
    elif choice == "2":
        friendship_ending()
    else:
        dragon_encounter()

def final_choice():
    global has_treasure

    print("\nYou find the crystal and a pile of treasure.")
    print("1. Take the crystal")
    print("2. Take the treasure")
    print("3. Use the crystal's power")

    choice = input("> ")

    if choice == "1":
        hero_ending()
    elif choice == "2":
        rich_ending()
    elif choice == "3":
        villain_ending()
    else:
        final_choice()

def hero_ending():
    print("\nHERO ENDING")
    print("You return the crystal and save the kingdom!")

def rich_ending():
    print("\nRICH ENDING")
    print("You leave with treasure and become wealthy.")

def friendship_ending():
    print("\nFRIENDSHIP ENDING")
    print("You make peace with the dragon and save the kingdom together.")

def villain_ending():
    print("\nVILLAIN ENDING")
    print("You use the crystal's power to rule the kingdom.")

def sacrifice_ending():
    print("\nSACRIFICE ENDING")
    print("You destroy the darkness but lose your life.")

def game_over():
    print("\nGAME OVER")
    print("Your adventure ends here.")

# Start the game
start_game()        



        
        