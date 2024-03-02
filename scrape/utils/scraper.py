import requests
from bs4 import BeautifulSoup
import re


class VLRScraper:
    @staticmethod
    def fetch_match_data():
        pass

    @staticmethod
    def fetch_round_data():
        pass

    @staticmethod
    def fetch_page_soup(url: str) -> BeautifulSoup:
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')

        return soup

    @staticmethod
    def save_soup_to_file(soup, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(soup.prettify())


if __name__ == '__main__':
    soup = VLRScraper.fetch_page_soup(
        'https://www.vlr.gg/303095/team-heretics-vs-karmine-corp-champions-tour-2024-emea-kickoff-playoffs-gf/')

    VLRScraper.save_soup_to_file(soup, 'soup.txt')
