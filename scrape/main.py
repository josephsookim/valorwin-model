from utils.scraper import VLRScraper

if __name__ == '__main__':
    soup = VLRScraper.fetch_page_soup(
        'https://www.vlr.gg/303095/team-heretics-vs-karmine-corp-champions-tour-2024-emea-kickoff-playoffs-gf/?game=all&tab=economy')

    match = VLRScraper.fetch_match_data(soup)

    # VLRScraper.save_soup_to_file(maps[1], 'soup.txt')
