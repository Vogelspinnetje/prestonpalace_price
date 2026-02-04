'''
Author: Yesse Monkou
Date: 04/02/2026

Description:
This script retrieves price data from Preston Palace for 1 person for 1 night. 
'''

import requests
from datetime import date, timedelta

def scrape(timespan: str=28, price_cap: int=105) -> list:
    """This script retrieves the price data from Preston Palace for 1 person for 1 night.

    Args:
        timespan (str, optional): Days to look ahead. Defaults to 28.
        price_cap (int, optional): Max price. Defaults to 105.

    Returns:
        list: Date\tPrice
    """
    url: str = f"https://www.prestonpalace.nl/price_rates.json?period%5Bstart%5D={date.today()}&period%5Bend%5D={date.today() + timedelta(days=1)}&party%5Badults%5D=1&range%5Bpage%5D=0&range%5Blimit%5D={timespan}"

    headers: dict = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }
    r = requests.get(url, headers=headers)
    data: dict = r.json()
    pricelist: list = []
    
    for i in range(len(data["rates"])):
        price: float = float(data["rates"][i]["bar"]["price"].replace(",", "."))
        if price < price_cap:
            pricelist.append(f'{data["rates"][i]["date"]}\t{price}')
    
    return pricelist

if __name__ == "__main__":
    print(scrape(28,110))