from scrapers.Kamernet import Kamernet
from scrapers.Pararius import Pararius
from scrapers.Huurwoningen import Huurwoningen
from scrapers.Funda import Funda
from storage import AdvertStorage
import time
from datetime import datetime

minutes = 1

SCRAPERS = [
    Kamernet(),
    Pararius(),
    Huurwoningen(),
    # Funda()
]

def main():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"\nTime: {current_time} | Running scan...")
        
        storage = AdvertStorage()
        for scraper in SCRAPERS:
            adverts = scraper.fetch_new_adverts()
            for advert in adverts:
                if storage.is_new_advert(advert):
                    print('New advert found:', advert)
                    storage.save_advert(advert)
        storage.close()
        time.sleep(minutes * 60)

if __name__ == '__main__':
    main() 