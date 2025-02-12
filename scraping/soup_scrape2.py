import requests
from bs4 import BeautifulSoup
import json
import sys

def get_schedule(season: str, team: str):
    # Adjust the URL to use the /text format
    URL = f"https://goheels.com/sports/{team}/schedule/text"

    # Try making a request
    # HEADERS = {"User-Agent": "Mozilla/5.0"}
    RESPONSE = requests.get(URL) #, headers=HEADERS)

    # if the page is not accessed, kill the program
    if RESPONSE.status_code != 200:
        print("Error. Status code: " + RESPONSE.status_code)    
        return json.dumps({"error": f"Failed to retrieve schedule for {team} ({season})"})

    # HTML parser
    SOUP = BeautifulSoup(RESPONSE.text, "html.parser")
    
    with open(f"{team}_{season}.html", "w") as fp:
        json.dump(RESPONSE.text, fp)
        exit()
    
    # get all text on the webpage into a list
    page_text: list[str] = []
    for div in SOUP.find_all("div"):
        for elem in div.find_all(True):
            print(elem)
            page_text.append(elem.text)
    
    
    return page_text

    # Get raw text from the response
    # schedule_text = RESPONSE.text.strip()

    # Split the text by lines and clean it up
    # lines = schedule_text.split("\n")
    # games = [line.strip() for line in lines if line.strip()]

    # return json.dumps(games)

# for running the program from command line
if __name__ == "__main__":
    # insufficient number of parameters. Kill the program
    if len(sys.argv) < 3:
        print(json.dumps({"error": "Missing arguments. Usage: python script.py <season> <team>"}))
        sys.exit(1)

    # assign parameters and call function (could be one line)
    season = sys.argv[1]
    team = sys.argv[2]
    print(get_schedule(season, team))
