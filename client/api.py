import requests

from bs4 import BeautifulSoup


from hammer import config

html = None

def get_html():
  req = requests.get(URL)
  soup = BeautifulSoup(req.text)

  global html
  html = soup.body


def get_data():
  get_html()

  addr = {}
  # get html from website
  
  # get formatted data config
  data = html.h2.get_text().strip().split(':')

  try: addr["host"] = data[0]
  except: addr["host"] = '77.88.55.55'

  try: addr["port"] = int(data[1])
  except: addr["port"] = 80

  return addr


def is_needed():
  if html is None:
    get_html()

  needed = html.h1.get_text().strip()

  return needed.upper() == 'YES'