import pyperclip
import time
from pynput.keyboard import Controller, Key

def paste(toPaste):
    for char in toPaste:
        # print(char)
        keyboard.tap(char)
        time.sleep(0.025)

if __name__ == "__main__":
    keyboard = Controller()

    toPaste = pyperclip.paste()
    pyperclip.copy(toPaste)
    # print(toPaste)
    time.sleep(5)
    paste(toPaste)