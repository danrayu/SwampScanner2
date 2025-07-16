from scrapers.Kamernet import Kamernet
from scrapers.Pararius import Pararius
from scrapers.Huurwoningen import Huurwoningen
from scrapers.Funda import Funda
from storage import AdvertStorage
import time
from datetime import datetime
import json
from notifier import notify
minutes = 1

SCRAPERS = [
    Kamernet(),
    Pararius(),
    Huurwoningen(),
    # Funda()
]

def get_config():
    with open("config.json", 'r') as file:
        return json.load(file)
    

def main():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"\nTime: {current_time} | Running scan...")
        
        storage = AdvertStorage()
        
        all_adverts = []
        for scraper in SCRAPERS:
            adverts = scraper.fetch_new_adverts()
            for advert in adverts:
                if storage.is_new_advert(advert):
                    print('New advert found:', advert)
                    storage.save_advert(advert)
                    all_adverts.append(advert)
                    
        storage.close()
                    
        config = get_config()
        if len(all_adverts) > 0:
            notify(all_adverts, config["recipient_emails"], config["email_credentials"])
        else:
            print("No ads detected.")
        
        time.sleep(minutes * 10)

if __name__ == '__main__':
    main() 