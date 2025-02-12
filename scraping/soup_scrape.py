from bs4 import BeautifulSoup
import requests
import json

# Define the site page and retrieve the HTML data
# URL = "https://goheels.com/sports/baseball/schedule/text" # Baseball schedule
season = "2024-25"
team = "mens-basketball"


def team_stats(season: str, team: str) -> list[str]:
    """given the team and season, parses the UNC athletics website to get team data."""

    # storing the html page returned (not dynamic -> selenium)
    URL = f"https://goheels.com/sports/{team}/stats/{season}"
    RESPONSE = requests.get(URL)

    # if request failed, stop the process (error handling)
    if (RESPONSE.status_code != 200):
        print("Error. Status code: " + RESPONSE.status_code)    
        exit()
        
    SOUP = BeautifulSoup(RESPONSE.text, "html.parser")
    # add each element found to the list
    full_list: list[str] = []
    for tag in SOUP.find_all("td"):

        # separate any elems from new lines and whitespace
        filtered_tag: list[str] = tag.text.split('\n')
        for elem in filtered_tag:
            if (elem.strip() != ''):
                full_list.append(elem.strip())
    
    # storing the main types of data from UNC athletics site
    full_dict: dict[list[str]] = {"Scoring": [], "Shooting": [],  "Rebounding": [], "Assists": [], "Steals": [], "Blocks": [], "Attendance":[]}
    idx: int = 1

    for header in full_dict:
        # move to next header when it is seen
        while (idx < len(full_list) and not full_list[idx] in full_dict):
            full_dict[header].append(full_list[idx])
            idx += 1
        idx +=1 

    # write to a json file
    with open(f"{team}_{season}.json", "w") as fp:
        json.dump(full_dict , fp) 
    
    # return the resulting diction
    return full_list


# for debuging purposes
# print(team_stats(season=season, team=team))