# Dependencies
import requests
from bs4 import BeautifulSoup
import re
from typing import List, Tuple
from utils.database import MongoDB

# Models
from models.Match import Match
from models.Map import Map
from models.Round import Round

mongo = MongoDB()


class VLRScraper:
    @staticmethod
    def fetch_page_match_urls(soup: BeautifulSoup) -> List[str]:
        match_soups = soup.find_all('a', {'class': 'wf-module-item'})
        match_urls = []

        for match_tag in match_soups:
            href = match_tag.get('href')
            match_urls.append(f'https://www.vlr.gg{href}')

        return match_urls

    @staticmethod
    def fetch_match_data(soup: BeautifulSoup) -> Match:
        match = Match()
        map_names = VLRScraper.fetch_map_names(soup)

        map_soups = soup.find_all(
            'table', {'class': 'wf-table-inset mod-econ'})

        map_number = 0
        for map_soup in map_soups:
            if VLRScraper.is_valid_map_table(map_soup):
                match.maps.append(VLRScraper.fetch_map_data(
                    map_soup, map_names[map_number]))

                map_number += 1

        return match

    @staticmethod
    def fetch_map_data(map_soup: BeautifulSoup, map_name: str) -> Map:
        round_soups = map_soup.find_all('td')
        round_tables = []

        for round_soup in round_soups:
            if VLRScraper.is_valid_round_table(round_soup):
                round_tables.append(round_soup)

        # get map winner
        _, map_outcome = VLRScraper.fetch_round_data(
            round_tables[-1], -1, -1)

        map = Map(map_name, map_outcome)

        team_score = 0
        enemy_score = 0
        for round_table in round_tables:
            round, round_winner = VLRScraper.fetch_round_data(
                round_table, team_score, enemy_score)

            if round_winner == 1:
                team_score += 1

            else:
                enemy_score += 1

            map.rounds.append(round)

        # Save to Database
        mongo.add_map_data(map)

        return map

    @staticmethod
    def fetch_round_data(round_soup: BeautifulSoup, team_score, enemy_score) -> Tuple[Round, int]:
        loadouts = round_soup.find_all('div', {'class': 'bank'})

        team_loadout = VLRScraper.categorize_loadout(
            loadouts[0].get_text(strip=True))
        enemy_loadout = VLRScraper.categorize_loadout(
            loadouts[1].get_text(strip=True))

        round_outcome = VLRScraper.fetch_round_winner(round_soup)

        round = Round(team_loadout, enemy_loadout,
                      team_score, enemy_score, round_outcome)

        return round, round_outcome

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
