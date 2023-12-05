import json, os

path = "C:/Users/disgu/Documents/Projects/Python/PythonOS"


def create_file(username, file_name, location, file_type):
    try:
        open(f"{path}/data/users/{username}/{location}/{file_name}.{file_type}", "x")

        open(f"{path}/data/users/{username}/{location}/{file_name}.{file_type}", "w").write("""
  _____       _   _                  ____   _____ 
|  __ \     | | | |                / __ \ / ____|
| |__) |   _| |_| |__   ___  _ __ | |  | | (___  
|  ___/ | | | __| '_ \ / _ \| '_ \| |  | |\___ \ 
| |   | |_| | |_| | | | (_) | | | | |__| |____) |
|_|    \__, |\__|_| |_|\___/|_| |_|\____/|_____/ 
         _/ |                                    
        |___/                                     
                                  

File System by PythonOS - Disguised Fox (foreskin)
        """)
        return f"Created {file_name}.{file_type} in {location}"
    except FileExistsError as e:
        return "File already exists."
    except FileNotFoundError as e:
        return f"Failed to save temporary data to {file_name}.{file_type}"
def create_log(username, text, file_name):
    log_end = "log"
    try:
        open(f"{path}/data/users/{username}/This PC/Local Disk/Logs/{file_name}.{log_end}", "x")

        open(f"{path}/data/users/{username}/This PC/Local Disk/Logs/{file_name}.{log_end}", "w").write(f"""

  _____       _   _                  ____   _____ 
|  __ \     | | | |                / __ \ / ____|
| |__) |   _| |_| |__   ___  _ __ | |  | | (___  
|  ___/ | | | __| '_ \ / _ \| '_ \| |  | |\___ \ 
| |   | |_| | |_| | | | (_) | | | | |__| |____) |
|_|    \__, |\__|_| |_|\___/|_| |_|\____/|_____/ 
         _/ |                                    
        |___/                                     
                                  

File System by PythonOS - Disguised Fox (foreskin)
                                                                                                       
-=====> LOG START <=====-


                                                                                                    
{text}
                                                                                            


-=====> LOG END <=====-
        """)
        return f"Created log with name {file_name} and text {text}"
    except FileExistsError as e:
        return f'Failed to create log with exception {e}'
    except FileNotFoundError as e:
        return f'Log File failed to save: {e}'


def edit_file(username, location, text, file_name, file_type):
    try:
        open(f"{path}/data/users/{username}/{location}/{file_name}.{file_type}", "w").write(f"""
    _____       _   _                  ____   _____ 
    |  __ \     | | | |                / __ \ / ____|
    | |__) |   _| |_| |__   ___  _ __ | |  | | (___  
    |  ___/ | | | __| '_ \ / _ \| '_ \| |  | |\___ \ 
    | |   | |_| | |_| | | | (_) | | | | |__| |____) |
    |_|    \__, |\__|_| |_|\___/|_| |_|\____/|_____/ 
            _/ |                                    
            |___/                                     
                                    

    File System by PythonOS - Disguised Fox (foreskin)

    -=====> EDIT START <=====-


    {text}
                                                                                            

    -=====> EDIT END <=====-
            """)
    except FileNotFoundError as e:
        return f'Failed to fetch {file_name}.{file_type} ({e})'
    
def remove_file(username, file_name, file_type, location):
    try:
        os.remove(f"{path}/data/users/{username}/{location}/{file_name}.{file_type}")
        return f'Deleted {file_name}.{file_type} from {location}'
    except FileNotFoundError as e:
        return f'Failed to fetch {file_name}.{file_type} ({e})'