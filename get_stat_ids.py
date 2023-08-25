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

    stat_ids = []
    # Loop through all categories
    for category in json_data['props']['pageProps']['statOverview']['categories']:
        # Loop through all sub-categories within a category
        for sub_category in category['subCategories']:
            # Loop through all stats within a sub-category
            for stat in sub_category['stats']:
                # Gather the statId
                stat_id = stat['statId']
                stat_ids.append(stat_id)  # Append statId to the list
    
    # print(json_data['props']['pageProps'].keys())
    # print(json_data['props']['pageProps']['statDetails'].keys())
    # statDetails keys:
    # ['tourCode', 'year', 'displaySeason', 'statId', 'statType', 'tournamentPills', 'yearPills', 'statTitle', 'statDescription', 'tourAvg', 'lastProcessed', 'statHeaders', 'statCategories', 'rows', 'sponsorLogo']
    # print(json_data['props']['pageProps']['statOverview']['categories'][0])
else:
    print("Script tag with JSON data not found.")

print(len(stat_ids))

with open('stat_ids.json', 'w') as f:
    json.dump(stat_ids, f)

# with open('stat_ids.json', 'r') as f:
#     stat_ids_loaded = json.load(f)
