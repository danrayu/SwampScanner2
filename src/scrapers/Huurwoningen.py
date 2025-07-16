

from base_scraper import BaseScraper
from Advert import Advert
import requests
from bs4 import BeautifulSoup

class Huurwoningen(BaseScraper):
    BASE_URL = 'https://www.huurwoningen.nl/in/eindhoven/?price=800-2800&bedrooms=3'
    
    def fetch_new_adverts(self):
        adverts = []
        response = requests.get(self.BASE_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        for listing in soup.select('[class*="search-list__item search-list__item--listing"]'):
            page_url = "https://www.huurwoningen.nl" + listing.select_one('a')["href"]

            title = listing.select_one('.listing-search-item__title').get_text(strip=True)
            price = self.clean_price((listing.select_one('.listing-search-item__price').get_text(strip=True)))
            location = listing.select_one('.listing-search-item__sub-title').get_text(strip=True)
            date_posted = None
            adverts.append(Advert(page_url, title, price, location, date_posted))
        return adverts 
    