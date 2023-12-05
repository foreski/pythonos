import json, time, os
from modules.users.users import create_user, remove_user, login_user, change_user, get_data, verify_user

os.system("title " + "Python-OS [v1.0-Latest]")
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

        

    """


    print(menu_screen)

    l = input("Login (y/n) : ")
    s = input("Verify (y/n) : ")


    if l == 'n' and s == 'n':
        username = input("What would your username/name be? : ")
        password = input("What's your password going to be? : ")
        reenter_pass = input("Please type your password again : ")

        if password == reenter_pass or reenter_pass == password:
            r = create_user(username, password, reenter_pass)
            print(
                r + "\n\nReturning to main screen."
            )

            time.sleep(1.1)
            os.system("cls||clear")
            time.sleep(0.2)
            main_menu()
        else:
            print("Your password doesn't match!")

            time.sleep(1.5)
            os.system("cls||clear")
            time.sleep(0.2)
            main_menu()
    elif l == 'y' and s == 'n':
        username = input("What's your username? : ")
        password = input("What's your password? : ")

        r = login_user(username, password)
    elif l == 'n' and s == 'y':
        username = input("What's your username? : ")
        password = input("What's your password? : ")
        ss = verify_user(username, password)

        print(
            ss + "\n\nReturning to main screen."
        )
        time.sleep(1.1)
        os.system("cls||clear")
        time.sleep(0.2)
        main_menu()
    else:
        print("[ERROR]: The script failed to interpet False to True.")
main_menu()