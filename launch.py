import json, time, os, keyboard, requests
from modules.users.users import users, get_data

vers = requests.get("https://foreskin.icu/data/pyversion")
os.system("title " + "Python-OS [v1.0]")

def full_screen():
    keyboard.press('f11')
def main_menu():
    menu_screen = """

  _____       _   _                  ____   _____ 
 |  __ \     | | | |                / __ \ / ____|
 | |__) |   _| |_| |__   ___  _ __ | |  | | (___  
 |  ___/ | | | __| '_ \ / _ \| '_ \| |  | |\___ \ 
 | |   | |_| | |_| | | | (_) | | | | |__| |____) |
 |_|    \__, |\__|_| |_|\___/|_| |_|\____/|_____/ 
         __/ |                                    
        |___/                                     
This command prompt has been placed in 'Full Screen' to make it feel like a actual operating system.
        

    """


    print(menu_screen)
    usernames = []
    full_screen()
    for filename in os.listdir(f"./data/users/"):
        if filename == "usernames.txt":
            pass
        else:
            usernames.append(filename)
    for i, itm in enumerate(usernames, start=1):
        print(f"{i}) {itm}")

    account = input("\nWhich account? : ")
main_menu()
