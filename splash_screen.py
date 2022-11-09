import os
import time
import pyfiglet as pyfig


def splash_screen(message, seconds):
    ascii_separator = ("=" * 75)
    screen_text = pyfig.figlet_format(message)
    print("\n")
    print(ascii_separator)
    print(screen_text)
    print(ascii_separator)
    time.sleep(seconds)
    os.system('cls')


splash_screen("Message", 5)
username = input("Enter Username:")
