"""
A class representing an ad of a apartment / home
"""

class Advert:
    def __init__(self, page_url, title=None, price=None, location=None, date_posted=None):
        self.page_url = page_url
        self.title = title
        self.price = price
        self.location = location
        self.date_posted = date_posted

    def __repr__(self):
        return f"Advert(title={self.title}, price={self.price}, location={self.location}, url={self.page_url}, date_posted={self.date_posted})" 