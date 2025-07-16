from abc import ABC, abstractmethod
from typing import List
from Advert import Advert

class BaseScraper(ABC):
    def __init__(self, BASE_URL = None):
        if BASE_URL != None:
            self.BASE_URL = BASE_URL
    
    @abstractmethod
    def fetch_new_adverts(self) -> List[Advert]:
        """
        Fetch new adverts from the website.
        Returns a list of Advert objects.
        """
        pass 
    
    def clean_price(self, text):
        end_string = ""
        for char in text:
            if char.isnumeric():
                end_string += char
        return end_string