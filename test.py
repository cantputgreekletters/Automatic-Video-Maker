file_loc = "L:\Code\AutomaticVideoMaker\\redditId.json"
import json
with open (file_loc,"r") as file:
    data = json.load(file)

print(data["client_id"])