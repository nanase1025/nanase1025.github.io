import json
import os
import sys
from datetime import datetime

import requests
from bs4 import BeautifulSoup

SCHOLAR_ID = os.environ['GOOGLE_SCHOLAR_ID']
PROFILE_URL = f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en"
BROWSER_HEADERS = {
    'User-Agent': (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    ),
    'Accept-Language': 'en-US,en;q=0.9',
}


def fetch_direct():
    response = requests.get(PROFILE_URL, headers=BROWSER_HEADERS, timeout=60)
    response.raise_for_status()
    return response.text


def fetch_via_scraperapi():
    api_key = os.environ.get('SCRAPER_API_KEY')
    if not api_key:
        return None
    # Scholar is a "protected domain" for ScraperAPI, which requires premium.
    payload = {'api_key': api_key, 'url': PROFILE_URL, 'premium': 'true'}
    response = requests.get('https://api.scraperapi.com/', params=payload, timeout=180)
    response.raise_for_status()
    return response.text


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    stats = soup.find_all('td', class_='gsc_rsb_std')
    name_elem = soup.find('div', id='gsc_prf_in')
    if not stats or not name_elem:
        return None
    return name_elem.text, int(stats[0].text)


def scrape():
    for fetch in (fetch_direct, fetch_via_scraperapi):
        try:
            html = fetch()
        except Exception as exc:
            print(f"{fetch.__name__} failed: {exc}", file=sys.stderr)
            continue
        if html is None:
            continue
        parsed = parse(html)
        if parsed:
            print(f"Fetched via {fetch.__name__}")
            return parsed
        print(f"{fetch.__name__} returned a page without profile stats", file=sys.stderr)
    return None


result = scrape()
if result is None:
    # Exiting here skips the push, so the last good numbers stay published.
    sys.exit('Could not read the Scholar profile. Published stats left unchanged.')

name, citations = result
print(f"Name: {name}, Citations: {citations}")

os.makedirs('results', exist_ok=True)

with open('results/gs_data_shieldsio.json', 'w') as f:
    json.dump({'schemaVersion': 1, 'label': 'citations', 'message': str(citations)}, f)

with open('results/gs_data.json', 'w') as f:
    json.dump(
        {'name': name, 'citedby': citations, 'updated': str(datetime.now())},
        f,
        ensure_ascii=False,
    )
