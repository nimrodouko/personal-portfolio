import json
import requests
def projectdisplay():
    mainurl = "https://api.github.com/users/nimrodouko/repos"
    response = requests.get(mainurl)
    if response.status_code == 200:
        data_returned = response.json()
        removed_data = [
            {"name":repo["name"],
             "fullname":repo["full_name"],
             "language":repo["language"],
             }
        for repo in data_returned
        ]
        return removed_data


    

print(projectdisplay())
