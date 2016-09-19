import requests

from bs4 import BeautifulSoup

import config

class API:
  def __init__(self):
    html = self.get_html()

  def get_html(self):
    req = requests.get(config.URL)
    soup = BeautifulSoup(req.text)

    global html
    html = soup.body


  def get_data(self):
    addr = {}
    # get html from website
    
    # get formatted data config
    data = html.h2.get_text().strip().split(':')

    try: addr["host"] = data[0]
    except: addr["host"] = '77.88.55.55'

    try: addr["port"] = int(data[1])
    except: addr["port"] = 80

    return addr


  def is_needed(self):
    needed = html.h1.get_text().strip()

    return needed.upper() == 'YES'