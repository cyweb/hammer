from ddos import main as ddos
import api

def main():
  data = api.get_data()

  ddos(_host=data["host"], _port=data["port"])

if __name__ == '__main__':
  main()