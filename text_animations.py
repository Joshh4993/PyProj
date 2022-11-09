import os
import time
from random import randint

die     = ["   \n O \n   "]  # 1
die.append("  O\n   \nO  ")  # 2
die.append("O  \n O \n  O")  # 3
die.append("O O\n   \nO O")  # 4
die.append("O O\n O \nO O")  # 5
die.append("O O\nO O\nO O")  # 6

def rocket_animation():
    distance_from_top = 10
    while True:
        print("\n" * distance_from_top)
        print("          /\        ")
        print("          ||        ")
        print("          ||        ")
        print("         /||\        ")
        time.sleep(0.2)
        os.system('cls')
        distance_from_top -= 1
        if distance_from_top < 0:
            distance_from_top = 10

def animate_text(text):
    number_of_charaters = 1
    while True:
        print("\n")
        print(text[0:number_of_charaters])
        number_of_charaters += 1
        if number_of_charaters > len(text):
            number_of_charaters = 0
        time.sleep(0.2)
        os.system('cls')

def roll_dice():
    for roll in range(0,15):
        os.system('cls')
        print("\n")
        number = randint(0,5)
        print(die[number])
        time.sleep(0.2)


#rocket_animation()
#animate_text("Hello World!")
#roll_dice()