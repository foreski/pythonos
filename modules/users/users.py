import json, random, os,shutil
from os import getcwd

with open("./data/data.json", "r") as ffff:
    config = json.load(ffff)
paths = ""
path = config["FolderDir"]
def create_user(username = None, password = None, reenter = None):
    os.system("title " + "Python-OS [Account Creation]")
    if username is None or password == None:
        return 'Please enter a username.'
    elif password is None or password == None:
        return 'Please enter a password.'
    elif reenter is None or reenter == None:
        return 'Please re-enter your password.'
    else:
        try:
            os.makedirs(f'{path}/data/users/{username}')
            open(f'{path}/data/users/{username}/{username}.json', 'x')
            open(f'{path}/data/users/username.txt', 'x')
            open(f'{path}/data/users/username.txt', 'w').write(f'{username}')
            open(f'{path}/data/users/{username}/{username}.json', 'w').write('{}')

            shutil.copytree(f"{path}/CopyFiles/Desktop", f"{path}/data/users/{username}/Desktop")
            shutil.copytree(f"{path}/CopyFiles/Downloads", f"{path}/data/users/{username}/Downloads")
            shutil.copytree(f"{path}/CopyFiles/Documents", f"{path}/data/users/{username}/Documents")
            shutil.copytree(f"{path}/CopyFiles/This PC", f"{path}/data/users/{username}/This PC")
            shutil.copytree(f"{path}/CopyFiles/Pictures", f"{path}/data/users/{username}/Pictures")
            shutil.copytree(f"{path}/CopyFiles/Network", f"{path}/data/users/{username}/Network")

            with open(f'{path}/data/users/{username}/{username}.json', 'r') as f:
                r = f.readline()
            return f'Created {username} on Python-OS'
        except FileExistsError as e:
            return f'Failed to copy files for {username} - {e}'
        except FileNotFoundError as e:
            return f'Failed to create files for {username} - {e}'
        
def verify_user(username, password):
    os.system("title " + "Python-OS [Account Verification]")
    try:
        data = {
            f"{username}": {
                "username": f"{username}",
                "password": f"{password}"
            }
        }

        with open(f"{path}/data/users/{username}/{username}.json", "w+") as fp:
            json.dump(data, fp, sort_keys=True, indent=4)
                                
        new = get_data(username)

        if username in new:
            return f"Created account for {username}!"
        elif username not in new:
            return f"Failed to add {username} to the OS!"
        else:
            return f'Failed to create user account with the name {username}.'
    except KeyError as e:
        return f'Failed to fetch {e}'
    except FileNotFoundError as e:
        return f'Local Files for {username} not found.'
def remove_user(username = None, password = None):
    os.system("title " + "Python-OS [Account Removal]")
    if username is None or password == None:
        return 'Please enter a username.'
    elif password is None or password == None:
        return 'Please enter a password.'
    else:
        try:
            os.remove(f'./data/users/{username.json}')
            return f'Removed {username} from users!'
        except FileNotFoundError as e:
            return f'Failed to remove {username} with exception : {e}'
def change_user(username, new_username, password):
    os.system("title " + "Python-OS [Username Change]")
    try:
        os.rename(f"{path}/data/users/{username}/{username}.json", f"./data/users/{username}/{new_username}.json")
        os.rename(f"./data/users/{username}", f"./data/users/{new_username}")
        return f'Changed username from {username} to {new_username}'
    except FileNotFoundError as e:
        return f'{username} wasn\'t found in local files!'
def login_user(username, password):
    os.system("title " + "Python-OS [Logging-In]")
    if os.path.exists(os.path.join(os.getcwd(), f'./data/users/{username}')):
        with open(f"{path}/data/users/{username}/{username}.json", "r") as f:
            s = json.load(f)
        passwords = s[str(username)]["password"]

        if password == passwords:
            try:
                os.system(f'cd {paths}/data/users/{username}/This PC/LocalDisk/PythonOS/ & run.bat')
                return True
            except KeyError as e:
                return f'Failed to fetch {e}'
        elif password != passwords:
            return 'Password is incorrect.'
    else:
        return False

def get_data(username):
    with open(f"./data/user/{username}/{username}.json", "r") as f:
        users = json.load(f)
    return users