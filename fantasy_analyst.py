import os
import json
import requests

LEAGUE_ID = os.environ.get("FANTASY_LEAGUE_ID")
ROSTER_ID = os.environ.get("FANTASY_ROSTER_ID")

def fetch_league_data():
    print("Fetching league data...")
    # Fetch Roster from Sleeper API
    roster_url = f"https://sleeper.app{LEAGUE_ID}/rosters"
    rosters = requests.get(roster_url).json()
    
    # Fetch Weekly Matchups
    matchup_url = f"https://sleeper.app{LEAGUE_ID}/matchups/1" 
    matchups = requests.get(matchup_url).json()
    
    # Fetch Trending Players
    trending_url = "https://sleeper.app"
    trending = requests.get(trending_url).json()

    data = {
        "rosters": rosters,
        "matchups": matchups,
        "trending_waivers": trending
    }
    
    with open("weekly_data.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Data saved successfully!")

if __name__ == "__main__":
    fetch_league_data()
