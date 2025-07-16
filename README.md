# Modular Real Estate Web Scraper

## Overview
This project is a modular web scraper for real estate rental websites. It is designed so that new website scrapers can be easily added by implementing a simple interface.

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the main scraper:
   ```bash
   python modules/main.py
   ```

## Adding a New Website Scraper
1. Create a new file in `modules/scrapers/` (e.g., `my_site.py`).
2. Subclass `BaseScraper` and implement the `fetch_new_adverts()` method to return a list of `Advert` objects.
3. Register your scraper in `modules/main.py` by adding it to the `SCRAPERS` list.

## Persistence
- Adverts are stored in a local SQLite database (`adverts.db`).
- Only new adverts (not seen before by URL) are printed and saved.

## Example
See `modules/scrapers/example_site.py` for a template. 