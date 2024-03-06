from utils.scraper import VLRScraper
from utils.database import MongoDB

if __name__ == '__main__':
    soup = VLRScraper.fetch_page_soup(
        'https://www.vlr.gg/event/matches/1925/champions-tour-2024-emea-kickoff/?series_id=3721')

    '''
    soup = VLRScraper.fetch_page_soup(
        'https://www.vlr.gg/299624/2game-esports-vs-co-op-gg-gamers-club-challengers-league-2024-brazil-split-1-regular-season-w3/?game=all&tab=economy')

    match = VLRScraper.fetch_match_data(soup)
    '''
