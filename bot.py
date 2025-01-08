import keyboard
import time
import pyautogui
from colorama import Fore, init
from pystyle import Colors, Write
import requests
import subprocess
import tqdm
import os
import json

# Inizializzare colorama
init(autoreset=True)

repo_path = 'C:/Users/simon/OneDrive/Desktop/RP/botlegna/treebot'
os.chdir(repo_path)

# File per memorizzare le credenziali
CREDENTIALS_FILE = 'credentials.json'

# Funzione per registrare le credenziali
def register_user():
    username = input(Fore.CYAN + "\nEnter a username: ")
    password = input(Fore.CYAN + "\nEnter a password: ")
    credentials = {"username": username, "password": password}
    
    # Salva le credenziali nel file JSON
    with open(CREDENTIALS_FILE, 'w') as f:
        json.dump(credentials, f)
    
    Write.Print(Fore.GREEN + "\nRegistration successful!", Colors.green)

# Funzione per fare il login
def login_user():
    with open(CREDENTIALS_FILE, 'r') as f:
        credentials = json.load(f)
    
    username = input(Fore.CYAN + "\nEnter your username: ")
    password = input(Fore.CYAN + "\nEnter your password: ")
    
    if username == credentials["username"] and password == credentials["password"]:
        Write.Print(Fore.GREEN + "\nLogin successful!", Colors.green)
        menu()
    else:
        Write.Print(Fore.RED + "\nIncorrect credentials. Please try again.", Colors.red)
        return False

# Funzione per gestire la registrazione o login
def handle_registration_or_login():
    if not os.path.exists(CREDENTIALS_FILE):  # Se il file delle credenziali non esiste
        Write.Print(Fore.YELLOW + "\nNo credentials found. Please register.", Colors.yellow)
        register_user()
    else:
        Write.Print(Fore.YELLOW + "\nCredentials found. Please login.", Colors.yellow)
        while not login_user():
            pass

# Esegui il git pull prima di avviare il bot
os.system('git pull')

def menu():
    title = r'''
 ____  ____    _____  ____  ____  _    
/  __\/  __\  /__ __\/  _ \/  _ \/ \   
|  \/||  \/|    / \  | / \|| / \|| |   
|    /|  __/    | |  | \_/|| \_/|| |_/\
\_/\_\\_/       \_/  \____/\____/\____/                                      
'''

    s = '''
    1. START BOT
    2. INFO
    3. EXIT
'''
    os.system("cls")
    print(Fore.RED + title)
    print(Fore.WHITE + s)
    scelta = input("\nEnter Choice:")
    if scelta == '1':
        os.system("cls")
        ask2()
    if scelta == '2':
        print("Version: 0.11")
        os.system("cls")
        menu()
    if scelta == '3':
        os.system("exit")

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
        time.sleep(29)

def ask2():
    print(Fore.GREEN + "Benvenuto nel RP TOOL by Simo!")
    print(Fore.YELLOW + "[ ! ] Premi 'b' per avviare il bot, premi 'm' per tornare indietro")
    while True:
        if keyboard.is_pressed('b'): 
            main()
            break
        if keyboard.is_pressed('m'): 
            menu()
            break

def ask():

    # Gestione registrazione o login
    handle_registration_or_login()

ask()
