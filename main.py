import random
import time

 # ● ┌ └ ┐ ¨2 └ ┘
 
dice_art = {
    1:("┌──────────┐",
       "|          |",
       "|     ●    |",
       "|          |",
       "└──────────┘"),

    2:("┌──────────┐",
       "|  ●       |",
       "|          |",
       "|       ●  |",
       "└──────────┘"),

    3: ("┌──────────┐",
        "| ●        |",
        "|     ●    |",
        "|        ● |",
        "└──────────┘"),

    4: ("┌──────────┐",
        "| ●     ●  |",
        "|          |",
        "| ●     ●  |",
        "└──────────┘"),

    5: ("┌──────────┐",
        "| ●      ● |",
        "|     ●    |",
        "| ●      ● |",
        "└──────────┘"),

    6: ("┌──────────┐",
        "| ●      ● |",
        "| ●      ● |",
        "| ●      ● |",
        "└──────────┘")
}  

dice = []
total = 0
print("================================")
print("     DICE ROLLING SIMULATOR     ")
print("================================")

time.sleep(0.5)
print("loading the program...")
time.sleep(0.5)
print("Welcome to the dice rolling simulator!")
time.sleep(0.5)
while True:
    num_of_dice = int(input("how many dice ? "))

    for die in range(num_of_dice):
        dice.append(random.randint(1,6))

    #for die in range(num_of_dice):
    #    for line in dice_art.get(dice[die]):
    #       print(line)
    print("rolling the dice...")
    time.sleep(0.5)
    for line in range(5):
        for die in dice:
            print(dice_art.get(die)[line],end="")
        print()
            
    for die in dice:
        total += die

    print(f"total : {total}") 

    while True : 
        choice = input("do you want to roll again ? (y/n) : ")
        if choice.lower() == "y":
            dice.clear()
            total = 0
            break
        elif choice.lower() == "n":
            print("exiting the program...")
            time.sleep(0.25)
            print("Thanks for playing!")
            time.sleep(0.25)
            print("===============================")
            time.sleep(0.25)
            exit()
        else:
            print("invalid input, please try again")
    






