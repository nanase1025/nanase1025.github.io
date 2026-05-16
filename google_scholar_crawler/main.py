import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

scholar_id = os.environ['GOOGLE_SCHOLAR_ID']
scraper_api_key = os.environ['SCRAPER_API_KEY']

url = f"https://scholar.google.com/citations?user={scholar_id}&hl=en"
payload = {'api_key': scraper_api_key, 'url': url}
response = requests.get('https://api.scraperapi.com/', params=payload)

soup = BeautifulSoup(response.text, 'html.parser')

stats = soup.find_all('td', class_='gsc_rsb_std')
citations = int(stats[0].text) if stats else 0

name_elem = soup.find('div', id='gsc_prf_in')
name = name_elem.text if name_elem else scholar_id

print(f"Name: {name}, Citations: {citations}")

os.makedirs('results', exist_ok=True)

shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": str(citations),
}
with open('results/gs_data_shieldsio.json', 'w') as f:
    json.dump(shieldio_data, f)

author_data = {
    "name": name,
    "citedby": citations,
    "updated": str(datetime.now()),
}
with open('results/gs_data.json', 'w') as f:
    json.dump(author_data, f, ensure_ascii=False)
