from utils.scraper import VLRScraper
from utils.database import MongoDB
import time
import os

if __name__ == '__main__':
    url_list = []

    with open('scrape/data/events.txt', 'r') as file:
        i = 1
        for url in file:
            try:
                soup = VLRScraper.fetch_page_soup(url.strip())
                urls = VLRScraper.fetch_page_match_urls(soup)
                url_list.extend(urls)
                print(f'done {i}', len(urls))

            except:
                print(f'error {i}')

            finally:
                i += 1
                time.sleep(1)

    with open('scrape/data/results.txt', 'w') as file:
        # Iterate through each URL in the list
        for url in url_list:
            # Write each URL to the file, followed by a newline character
            file.write(url + '\n')

    '''
    soup = VLRScraper.fetch_page_soup(
        'https://www.vlr.gg/299624/2game-esports-vs-co-op-gg-gamers-club-challengers-league-2024-brazil-split-1-regular-season-w3/?game=all&tab=economy')

    match = VLRScraper.fetch_match_data(soup)
    '''
