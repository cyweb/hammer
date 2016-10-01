import requests
import sys
import json

sys.path.insert(0, r'../')

from server import config

class API:
  def __init__(self):
    self.data = {}

  def get_data(self):
    # get html from website

    req = requests.get(config.URL)

    # get formatted data
    self.data = dict(json.loads(req.text))

    return self.data


  def is_needed(self):
    self.get_data()
    needed = self.data["needed"]
    return needed.upper() == 'YES'