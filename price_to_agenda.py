'''
Author: Yesse Monkou
Date: 04/02/2026

Description:
This script calls price_scaper to get prices and dates. Then these prices and dates are converted into ics standardized events. 
'''

from ics import Calendar, Event
from datetime import timedelta
from price_scraper import scrape

def to_agenda(ics_path: str):
    """This script calls price_scaper to get prices and dates. Then these prices and dates are converted into ics standardized events. 

    Args:
        ics_path (str): Path to .ics file
    """
    with open(ics_path, "r") as fh:
        c = Calendar(fh.read())
    
    info: list = scrape(timespan=28, price_cap=110)
    
    for hit in info:
        date: str = hit.split("\t")[0]
        price: str = hit.split("\t")[1]
        
        e = Event()
        e.uid = date
        e.name = price
        e.begin = date 
        e.make_all_day()
        e.url = "https://www.prestonpalace.nl"
        
        existing = next((evt for evt in c.events if evt.uid == date), None)
        if existing:
            c.events.remove(existing)
        
        c.events.add(e)
    
    with open(ics_path, "w") as fh:
        fh.writelines(c.serialize_iter())

if __name__ == "__main__":
    with open("ics_path.txt", "r") as fh:
        path: str = fh.read()
        
    to_agenda(path)