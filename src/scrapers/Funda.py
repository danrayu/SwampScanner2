

from base_scraper import BaseScraper
from Advert import Advert
import requests
from bs4 import BeautifulSoup

class Funda(BaseScraper):
    BASE_URL = 'https://www.funda.nl/zoeken/huur?selected_area=[%22eindhoven%22]&price=%220-2800%22&object_type=[%22apartment%22,%22house%22]&bedrooms=%223-%22&sort=%22date_down%22'
    
    def fetch_new_adverts(self):
        adverts = []
        response = requests.get(self.BASE_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        print(soup.body.find_all(text="Selecteer buurten"))
        target = soup.find(string=lambda text: "Selecteer buurten" in text)
        if target:
            parent = target
            div_count = 0
            while parent and div_count < 4:
                parent = parent.parent
                div_count += 1
            if parent and div_count == 2:
                print("Found the target 2 divs up!")
                print(parent.prettify())
            else:
                print("Could not find two divs up.")
        else:
            print("Text not found.")

        holding_frame = soup.select('[class*="flex flex-col gap-3 mt-4"]')
        print(holding_frame)
        for listing in holding_frame.findChildren("div" , recursive=False):
            page_url = "https://www.funda.nl" + listing.select_one('a')["href"]

            title = listing.select_one('[class*="flex font-semibold"]').select_one("span").get_text(strip=True)
            price = self.clean_price((listing.select_one('[class*="font-semibold mt-2 mb-0"]').select_one("div").get_text(strip=True)))
            location = listing.select_one('.truncate text-neutral-80').get_text(strip=True)
            date_posted = None
            adverts.append(Advert(page_url, title, price, location, date_posted))
        return adverts 
    