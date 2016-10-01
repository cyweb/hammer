import requests
from bs4 import BeautifulSoup
import sys

sys.path.insert(0, r'../')

from server import config

class API:
  def __init__(self):
    html = self.get_or_update_html()

  def get_or_update_html(self):
    req = requests.get(config.URL)
    soup = BeautifulSoup(req.text)

    self.html = soup.body


  def get_data(self):
    addr = {}
    # get html from website
    
    # get formatted data config
    data = self.html.h2.get_text().strip().split(':')

    try: addr["host"] = data[0]
    except: addr["host"] = '77.88.55.55'

    try: addr["port"] = int(data[1])
    except: addr["port"] = 80

    return addr


  def is_needed(self):
    self.get_or_update_html()
    needed = self.html.h1.get_text().strip()
    return needed.upper() == 'YES'