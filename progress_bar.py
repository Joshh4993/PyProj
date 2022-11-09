import os
import time


def progress_bar(seconds):
    for progress in range(0, seconds+1):
        if progress is 0:
            percent = 0
        else:
            percent = ((progress / seconds) * 100)
        print("\n")
        print("Loading...")
        print("<" + ("=" * progress) + (" " * (seconds - progress)) + ">  " + f"{percent:.2f}%")
        print("\n")
        time.sleep(1)
        os.system('cls')


progress_bar(3)
print("Done")
