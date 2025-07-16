

from base_scraper import BaseScraper
from Advert import Advert
import requests
from bs4 import BeautifulSoup

class Kamernet(BaseScraper):
    BASE_URL = 'https://kamernet.nl/huren/huurwoningen-eindhoven?radius=3&minSize=0&maxRent=20&searchCategories=16%2C2'

    def fetch_new_adverts(self):
        adverts = []
        response = requests.get(self.BASE_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        for listing in soup.select('[class*="ListingCard_root"]'):
            page_url = "https://kamernet.nl" + listing['href']
            
            title = listing.select_one('.ListingCard_listingRow__Ek5ZC').get_text(strip=True)
            price = self.clean_price((listing.select('.ListingCard_listingRow__Ek5ZC')[2].get_text(strip=True)))
            location = title
            date_posted = None
            adverts.append(Advert(page_url, title, price, location, date_posted))
        return adverts 