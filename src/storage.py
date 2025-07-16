import sqlite3
from typing import List
from Advert import Advert

class AdvertStorage:
    def __init__(self, db_path='adverts.db'):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS adverts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                page_url TEXT UNIQUE,
                title TEXT,
                price TEXT,
                location TEXT,
                date_posted TEXT
            )
        ''')
        self.conn.commit()

    def is_new_advert(self, advert: Advert) -> bool:
        cur = self.conn.execute('SELECT 1 FROM adverts WHERE page_url = ?', (advert.page_url,))
        return cur.fetchone() is None

    def save_advert(self, advert: Advert):
        self.conn.execute(
            'INSERT OR IGNORE INTO adverts (page_url, title, price, location, date_posted) VALUES (?, ?, ?, ?, ?)',
            (advert.page_url, getattr(advert, 'title', None), getattr(advert, 'price', None), getattr(advert, 'location', None), getattr(advert, 'date_posted', None))
        )
        self.conn.commit()

    def close(self):
        self.conn.close() 