# Programmer Name: Oreoluwa Adebusoye
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 10/09/2024
# Program Name: The Quest for the Master Key
# What program does (purpose): It is an interactive text-based adventure game where players navigate a vibrant jungle,
# make critical decisions, solve puzzles, and ultimately seek the elusive Master Key to escape a magical realm.

# Output Greeting and Prompt user to enter a name
name = input("Greetings, brave adventurer! Before we embark on this thrilling journey, what is your name? ")

# Continue story
print(f"\nAh, {name}, a name that echoes with potential! You’ve just stumbled upon a mystical board game, ")
print(f"shrouded in mystery and legend. As you rolled the dice, a swirl of magic enveloped you, transporting you ")
print(f"to a vibrant jungle teeming with life, danger, and adventure. Though the unknown may seem daunting, remember:")
print(f"Within this jungle lies the key to your escape—the elusive Master Key.\n")

# Prompt user for another input
decision = input("As you venture deeper into the jungle, you come across a rushing river blocking your path. "
                 "\nThe water is swift and treacherous. Do you want to build a raft using nearby logs or try to swim across? (Type 'raft' or 'swim') ").lower().strip()

# Handling decision
if decision == "raft":
    print("\nYou gather logs and vines to construct a makeshift raft. Carefully, you push it into the water and climb aboard.")
    print("As you float down the river, the current is strong, but you manage to navigate through the rapids!")
    print("You arrive safely on the other side, but you’ll need to be cautious moving forward.")

elif decision == "swim":
    print("\nYou take a deep breath and plunge into the river. The water is cold and the current pulls at you fiercely. ")
    print("You swim with all your might, but it’s a struggle!")

    # Prompt user for confidence level
    confidence = float(input("Enter your confidence level to determine how well you manage (between 0.1 and 10.0): "))

    if confidence < 4.0:
        print("You did not have the enough confidence and drowned. Try again.")
        exit()
    elif 4.0 <= confidence <= 10.0:
        print("You swim skillfully and reach the other side with ease! Energized.")
    elif confidence > 10.0:
        print("You were overconfident and drowned. Try again.")
        exit()
else:
    print("That is not a valid answer. You are stuck in the jungle forever. Game over. Try again.")
    exit()

# Prompt user for another decision
decision = input("\nNow, before you is a mysterious cave and an ancient temple covered in vines. "
                 "Do you want to explore the cave or enter the temple? (Type 'cave' or 'temple') ").lower().strip()

# Handling cave decision
if decision == "cave":
    print(
        "\nYou cautiously approach the cave entrance. Inside, you find a hidden treasure! But be careful, there are dangers ahead. "
        "How many steps will you take to avoid traps? (Enter a number)")

    steps = int(input())

    if steps < 5 or steps < 0:
        print("You stumble over a hidden trap and fall! You are stuck in the jungle forever. Game over. Try again.")
        exit()
    elif 5 <= steps <= 10:
        print(
            f"You skillfully navigate through the cave and avoid the traps! You find the Master Key! Congratulations!")
    elif steps > 10:
        print(
            "You rush through the cave confidently, but you trigger a cave-in! You barely make it out and you are stuck in the jungle forever. Game over. Try again.")
        exit()
else:
    # Handling temple decision
    if decision == "temple":
        print("\nYou push aside the vines and enter the ancient temple. Inside, the air is thick with mystery. "
              "You see a large stone door with a riddle inscribed on it: 'What has keys but can't open locks?' (Type your answer)")

        riddle_answer = input().lower().strip()

        if riddle_answer == "piano":
            print(
                f"The door creaks open, revealing a chamber filled with artifacts! Among them, you find the Master Key! Congratulations!")
        else:
            print(
                "The door does not budge. You hear the sound of footsteps approaching! Do you want to hide or try to solve the riddle again? (Type 'hide' or 'solve')")
            answer = input().lower().strip()

            if answer == "hide":
                print("You are found, and you are captured. You are stuck in the jungle forever. Game over. Try again.")
                exit()
            elif answer == "solve":
                print("You take a moment and realize the answer is 'piano.' The door opens, revealing the Master Key!")
            else:
                print("You decided not to hide or solve so you are captured, and you are stuck in the jungle forever. Game over. Try again.")
                exit()
    else:
        print("You are captured, and you are stuck in the jungle forever. Game over. Try again.")
        exit()

# 9. Output End game message
print(f"\nWell-done {name}! You have successfully navigated the jungle and found the Master Key. You can now escape this magical realm!")