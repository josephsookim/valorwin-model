# Dependencies
import requests
from bs4 import BeautifulSoup
import re
from typing import List

# Models
from models.Match import Match
from models.Map import Map
from models.Round import Round


class VLRScraper:
    @staticmethod
    def fetch_match_data(soup: BeautifulSoup) -> Match:
        match = Match()
        map_names = VLRScraper.fetch_map_names(soup)

        map_soups = soup.find_all(
            'table', {'class': 'wf-table-inset mod-econ'})

        for map_soup in map_soups:
            if VLRScraper.is_valid_map_table(map_soup):
                match.maps.append(VLRScraper.fetch_map_data(map_soup))
                break

        return match

    @staticmethod
    def fetch_map_data(map_soup: BeautifulSoup) -> Map:
        map = Map()

        round_soups = map_soup.find_all('td')

        for round_soup in round_soups:
            if VLRScraper.is_valid_round_table(round_soup):
                map.rounds.append(VLRScraper.fetch_round_data(round_soup))

        return map

    @staticmethod
    def fetch_round_data(round_soup: BeautifulSoup) -> Round:
        '''
        we need to get

        self.map = map have to get prior in first function
        self.team_score = team_score = handle after
        self.enemy_score = enemy_score = handle after
        self.map_outcome = map_outcome = handle prior
        '''

        loadouts = round_soup.find_all('div', {'class': 'bank'})

        team_loadout = VLRScraper.categorize_loadout(
            loadouts[0].get_text(strip=True))
        enemy_loadout = VLRScraper.categorize_loadout(
            loadouts[1].get_text(strip=True))

        round_outcome = VLRScraper.fetch_round_winner(round_soup)

        pass

    # Helper Functions
    @staticmethod
    def fetch_map_names(soup: BeautifulSoup) -> List[str]:
        map_soups = soup.find_all('div', {'class': 'js-map-switch'})[1:]

        return [map_soup.find('div').get_text(strip=True)[1:] for map_soup in map_soups]

    @staticmethod
    def categorize_loadout(loadout: str) -> str:
        value = float(loadout[:-1])

        if value <= 5:
            return 'eco'
        elif 5 < value <= 10:
            return 'semi-eco'
        elif 10 < value <= 20:
            return 'semi-buy'
        else:
            return 'full-buy'

    @staticmethod
    def fetch_round_winner(round_soup: BeautifulSoup) -> int:
        # Find all div elements within the td element
        div_elements = round_soup.find_all('div', {'class': 'rnd-sq'})

        # Check the order of appearance of div elements to determine the winner
        if len(div_elements) >= 2:
            if div_elements[0].has_attr('class') and 'mod-win' in div_elements[0]['class']:
                return 1
            elif div_elements[1].has_attr('class') and 'mod-win' in div_elements[1]['class']:
                return 2
        return 0

    @staticmethod
    def is_valid_round_table(round_soup: BeautifulSoup) -> bool:
        div_elements = round_soup.find_all(
            'div', class_='ge-text-light round-num')

        if div_elements:
            return True

        return False

    @staticmethod
    def is_valid_map_table(map_soup: BeautifulSoup) -> bool:
        text_elements = map_soup.find_all(text=True)

        for text in text_elements:
            if '(BANK)' in text:
                return True
        return False

    @staticmethod
    def fetch_page_soup(url: str) -> BeautifulSoup:
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')

        return soup

    @staticmethod
    def save_soup_to_file(soup, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(soup.prettify())
