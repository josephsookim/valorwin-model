from utils.scraper import VLRScraper
from utils.database import MongoDB
import time
import os

if __name__ == '__main__':
    url_list = VLRScraper.load_list_from_file('scrape/data/results.txt')

    i = 1
    for url in url_list:
        try:
            soup = VLRScraper.fetch_page_soup(url)
            match = VLRScraper.fetch_match_data(soup)

            print(f'done {i}')

        except:
            print(f'error {i}')

        finally:
            i += 1
            time.sleep(1)

    '''
    soup = VLRScraper.fetch_page_soup(
        'https://www.vlr.gg/299624/2game-esports-vs-co-op-gg-gamers-club-challengers-league-2024-brazil-split-1-regular-season-w3/?game=all&tab=economy')

    match = VLRScraper.fetch_match_data(soup)
    '''
