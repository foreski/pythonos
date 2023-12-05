from applications.files import create_file, create_log, edit_file, remove_file
import os, time, shutil, random, json

with open("../data.json/", "r") as ffff:
    config = json.load(ffff)

path = config["FolderDir"]
file_name_log = random.randint(2020, 2023)
file_name_log_end = random.randint(1000, 5000)

def terminal(username):
    os.system("title " + "Python-OS [Terminal]")
    commands_list = [
        "osremove",
        "oscreate",
        "help"
    ]
    os.system('cls||clear')
    print("""
Python OS [Version 1.0]
(P) Python Corporation. All rights reserver.
          

    """)
    command = input(f"P:/Users/{username}> ")

    if command == "osremove":
        name = input("File Name : ")
        type = input("File Type : ")
        location = input("File Location: ")

        if location == "This PC":
            print("This directory requires 'ADMINISTRATOR' permissions to access")

            time.sleep(1.1)
            os.system("cls|||clear")
            terminal(username)
        elif location == "Desktop":
            s = remove_file(username, name, type, location)
            print("[Python-OS] " + f"{s}")
            create_log(username, f"{username} removed {name}.{type} from {location}", f"{file_name_log}-{file_name_log_end}")
            time.sleep(1.5)
            os.system("cls||clear")
            time.sleep(.2)
            terminal(username)
        elif location == "Documents":
            s = remove_file(username, name, type, location)
            print("[Python-OS] " + f"{s}")
            create_log(username, f"{username} removed {name}.{type} from {location}", f"{file_name_log}-{file_name_log_end}")
            time.sleep(1.5)
            os.system("cls||clear")
            time.sleep(.2)
            terminal(username)
        elif location == "Pictures":
            s = remove_file(username, name, type, location)
            print("[Python-OS] " + f"{s}")
            create_log(username, f"{username} removed {name}.{type} from {location}", f"{file_name_log}-{file_name_log_end}")
            time.sleep(1.5)
            os.system("cls||clear")
            time.sleep(.2)
            terminal(username)
        elif location == "Downloads":
            s = remove_file(username, name, type, location)
            print("[Python-OS] " + f"{s}")
            create_log(username, f"{username} removed {name}.{type} from {location}", f"{file_name_log}-{file_name_log_end}")
            time.sleep(1.5)
            os.system("cls||clear")
            time.sleep(.2)
            terminal(username)
    elif command == "oscreate":
        name = input("File Name : ")
        type = input("File Type : ")
        location = input("File Location: ")

        if location == "This PC":
            print("This directory requires 'ADMINISTRATOR' permissions to access")
            time.sleep(1.1)
            os.system("cls|||clear")
            terminal(username)
        elif location == "Desktop" or "desktop":
            s = create_file(username, name, location, type)
            print("[Python-OS] " + f"{s}")
            create_log(username, f"{username} created {name}.{type} in {location}", f"{file_name_log}-{file_name_log_end}")
            time.sleep(1.5)
            os.system("cls||clear")
            time.sleep(.2)
            terminal(username)
        elif location == "Documents" or "documents":
            s = create_file(username, name, location, type)
            print("[Python-OS] " + f"{s}")
            create_log(username, f"{username} created {name}.{type} in {location}", f"{file_name_log}-{file_name_log_end}")
            time.sleep(1.5)
            os.system("cls||clear")
            time.sleep(.2)
            terminal(username)
        elif location == "Pictures" or "pictures":
            s = create_file(username, name, location, type)
            print("[Python-OS] " + f"{s}")
            create_log(username, f"{username} created {name}.{type} in {location}", f"{file_name_log}-{file_name_log_end}")
            time.sleep(1.5)
            os.system("cls||clear")
            time.sleep(.2)
            terminal(username)
        elif location == "Downloads" or "Downloads":
            s = create_file(username, name, location, type)
            print("[Python-OS] " + f"{s}")
            create_log(username, f"{username} created {name}.{type} in {location}", f"{file_name_log}-{file_name_log_end}")
            time.sleep(1.5)
            os.system("cls||clear")
            time.sleep(.2)
            terminal(username)
    elif command == "osedit":
        name = input("File Name : ")
        type = input("File Type : ")
        text = input("File Text : ")
        location = input("File Location: ")

        sr = input("[Python-OS] This will overwrite all data in the file, are you sure? (y/n)")

        if sr == "y":
            r = edit_file(username, location, text, name)
            print("[Python-OS] " + f"{r}")

            time.sleep(1.5)
            os.system("cls||clear")
            time.sleep(0.3)
            terminal(username)
        elif sr == "n":
            print("[Python-OS] " + f"Retreating action")

            time.sleep(1.5)
            os.system("cls||clear")
            time.sleep(0.3)
            terminal(username)
        else:
            print("[Python-OS] " + f"Unknown Response")

            time.sleep(1.5)
            os.system("cls||clear")
            time.sleep(0.3)
            terminal(username)
    elif command == "help":
        print("""
'osremove',
'oscreate',
'osedit',
'help',
'update (depricated)',
'osget'
      
These are commands for the OS Terminal
""")

        input("\nPress any key to continue...")

        print("[Python-OS] Returning to Terminal [1]")
        time.sleep(0.6)
        os.system("cls||clear")
        time.sleep(0.2)
        terminal(username)
    elif command == "update":
        print("[Python-OS] Retrevieing update.")
        time.sleep(0.5)
        print("[Python-OS] Loading BOOTSTRAPPER")

        os.system("title " + "Python OS [BOOTSTRAPPER]")

        time.sleep(0.5)

        print("[Python-OS] 0.5% / 100%")
        os.system("cls||clear")
        time.sleep(0.8)
        print("[Python-OS] 9% / 100%")
        os.system("cls||clear")
        time.sleep(0.8)
        print("[Python-OS] 15% / 100%")
        os.system("cls||clear")
        time.sleep(0.8)
        print("[Python-OS] 25.8% / 100%")
        os.system("cls||clear")
        time.sleep(0.8)
        print("[Python-OS] 33.2% / 100%")
        os.system("cls||clear")
        time.sleep(0.8)
        print("[Python-OS] 56.9% / 100%")
        os.system("cls||clear")
        time.sleep(0.8)
        print("[Python-OS] 68.5% / 100%")
        os.system("cls||clear")
        time.sleep(0.8)
        print("[Python-OS] 85% / 100%")
        os.system("cls||clear")
        time.sleep(0.8)
        print("[Python-OS] 97.2% / 100%")
        os.system("cls||clear")
        time.sleep(0.8)
        print("[Python-OS] 1005% / 100%")
        os.system("cls||clear")
        time.sleep(0.8)
        print("[Python-OS] Traveling back to latest update [terminal]")
        time.sleep(0.3)
        shutil.copytree(f"{path}/CopyFiles/This PC", f"{path}/data/users/{username}/This PC")
        shutil.copytree(f"{path}/CopyFiles/This PC/Local Disk", f"{path}/data/users/{username}/This PC/Local Disk")
        create_log(username, f"{username} updated [Python-OS] in This PC/Local Disk", f"{file_name_log}-{file_name_log_end}")
        time.sleep(0.4)
        os.system("cls||clear")
        time.sleep(0.2)
        terminal(username)
    elif command == "" or command not in commands_list:
        print("[Python-OS] Unknown Command")
        os.system("cls||clear")
        time.sleep(0.2)
        terminal(username)
