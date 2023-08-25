
from bs4 import BeautifulSoup
import urllib.request
import json

url = 'https://www.pgatour.com/stats/'
# Fetch the HTML file
response = urllib.request.urlopen(url)
web_content = response.read()

# Parse HTML content with BeautifulSoup
soup = BeautifulSoup(web_content, 'lxml')

script_tag = soup.find('script', {'type': 'application/json', 'id': '__NEXT_DATA__'})
if script_tag:
    json_text = script_tag.string
    json_data = json.loads(json_text)
    
    stat_details = json_data.get('props', {}).get('pageProps', {}).get('statDetails', {})
    print(json_data['props']['pageProps'].keys())
    #print(json_data['props']['pageProps']['statDetails'].keys())
    #statDetails keys:
    #['tourCode', 'year', 'displaySeason', 'statId', 'statType', 'tournamentPills', 'yearPills', 'statTitle', 'statDescription', 'tourAvg', 'lastProcessed', 'statHeaders', 'statCategories', 'rows', 'sponsorLogo']
    print(json_data['props']['pageProps']['statOverview']['categories'][0])
    # print(stat_details)
    # # Retrieve and print 'year', 'statType', 'statTitle'
    # year = stat_details.get('year')
    # stat_type = stat_details.get('statType')
    # stat_title = stat_details.get('statTitle')
    
    # print(f"Year: {year}")
    # print(f"Stat Type: {stat_type}")
    # print(f"Stat Title: {stat_title}\n")
    
    # # Iterate through rows to print player info
    # rows = stat_details.get('rows', [])
    # for row in rows:
    #     player_id = row.get('playerId')
    #     player_name = row.get('playerName')
    #     country = row.get('country')
    #     rank = row.get('rank')
        
    #     print(f"Player ID: {player_id}, Player Name: {player_name}, Country: {country}, Rank: {rank}")
        
    #     # Access stats for each player
    #     for stat in row.get('stats', []):
    #         stat_name = stat.get('statName')
    #         stat_value = stat.get('statValue')
    #         color = stat.get('color')
            
    #         print(f"  - Stat Name: {stat_name}, Stat Value: {stat_value}, Color: {color}")
        
    #     print()  # For a new line between players

else:
    print("Script tag with JSON data not found.")


