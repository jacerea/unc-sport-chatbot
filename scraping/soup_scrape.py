from bs4 import BeautifulSoup
import requests
import json

# Define the site page and retrieve the HTML data
# URL = "https://goheels.com/sports/baseball/schedule/text" # Baseball schedule
season = "2024-25"
team = "mens-basketball"


def team_stats(season: str, team: str) -> list[str]:
    URL = f"https://goheels.com/sports/{team}/stats/{season}"
    RESPONSE = requests.get(URL)

    # if request failed
    if (RESPONSE.status_code != 200):
        print("Error. Status code: " + RESPONSE.status_code)    
        exit()
        
    # DATA = RESPONSE.json()
    # create and scrape site for data
    # store it in a list
    full_list: list[str] = []
    SOUP = BeautifulSoup(RESPONSE.text, "html.parser")
    for tag in SOUP.find_all("td"):
        # separate any elems from new lines and whitespace
        filtered_tag: list[str] = tag.text.split('\n')
        for elem in filtered_tag:
            if (elem.strip() != ''):
                full_list.append(elem.strip())
    
    
    full_dict: dict[list[str]] = {"Scoring": [], "Shooting": [],  "Rebounding": [], "Assists": [], "Steals": [], "Blocks": [], "Attendance":[]}
    idx: int = 1
    for header in full_dict:
        while (idx < len(full_list) and not full_list[idx] in full_dict):
            full_dict[header].append(full_list[idx])
            idx += 1
        idx +=1 
    print(full_dict)

    with open("mens-basketball-2425.json", "w") as fp:
        json.dump(full_dict , fp) 
    return full_list

(team_stats(season=season, team=team))