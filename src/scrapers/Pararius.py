

from base_scraper import BaseScraper
from Advert import Advert
import requests
from bs4 import BeautifulSoup

class Pararius(BaseScraper):
    BASE_URL = 'https://www.pararius.com/apartments/eindhoven/1000-2800/radius-1/3-bedrooms'
    
    def fetch_new_adverts(self):
        adverts = []
        response = requests.get(self.BASE_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        for listing in soup.select('[class*="search-list__item search-list__item--listing"]'):
            page_url = "https://www.pararius.com" + listing.select_one('a')["href"]

            title = listing.select_one('.listing-search-item__title').get_text(strip=True)
            price = self.clean_price((listing.select_one('.listing-search-item__price').get_text(strip=True)))
            location = listing.select_one('.listing-search-item__sub-title').get_text(strip=True)
            date_posted = None
            adverts.append(Advert(page_url, title, price, location, date_posted))
        return adverts 
    