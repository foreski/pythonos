from applications.os_handling import terminal
import json

with open("./data.json/", "r") as ffff:
    config = json.load(ffff)

path = config["FolderDir"]
with open(f"{path}/data/users/username.txt", "r") as r:
    username = r.read()

terminal(username)