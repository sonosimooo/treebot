import keyboard
import time
import pyautogui
from colorama import Fore

def main():
    while True:
        keyboard.press('w')
        pyautogui.mouseDown(button='right')
        time.sleep(28)

        keyboard.release('w')
        pyautogui.mouseUp(button='right')

        keyboard.press('s')
        time.sleep(29)
        keyboard.release('s')

        print("Movimento indietro completato. In attesa di 29 secondi...")
        time.sleep(29)

def ask():
    print(Fore.GREEN + "Benvenuto nel RP TOOL by Simo!")
    print(Fore.YELLOW + "[ ! ] Premi 'b' per avviare il bot.")

    while True:
        if keyboard.is_pressed('b'): 
            main()
            break

ask()
