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
    username = input(Fore.CYAN + "Enter a username: ")
    password = input(Fore.CYAN + "Enter a password: ")
    credentials = {"username": username, "password": password}
    
    # Salva le credenziali nel file JSON
    with open(CREDENTIALS_FILE, 'w') as f:
        json.dump(credentials, f)
    
    Write.Print(Fore.GREEN + "Registration successful!", Colors.green)

# Funzione per fare il login
def login_user():
    with open(CREDENTIALS_FILE, 'r') as f:
        credentials = json.load(f)
    
    username = input(Fore.CYAN + "Enter your username: ")
    password = input(Fore.CYAN + "Enter your password: ")
    
    if username == credentials["username"] and password == credentials["password"]:
        Write.Print(Fore.GREEN + "Login successful!", Colors.green)
        return True
    else:
        Write.Print(Fore.RED + "Incorrect credentials. Please try again.", Colors.red)
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

def ask():
    handle_registration_or_login()
    print(Fore.GREEN + "Benvenuto nel RP TOOL by Simo!")
    print(Fore.YELLOW + "[ ! ] Premi 'b' per avviare il bot.")

    # Gestione registrazione o login

    while True:
        if keyboard.is_pressed('b'): 
            main()
            break

ask()
