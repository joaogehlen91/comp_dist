from bottle import route, run, request, redirect, view, get
import json
import sys
import time
import requests
import threading

messages = []
peers = sys.argv[2:]
peer = sys.argv[1]

@get('/get_peers')
def get_peers():
	return json.dumps(peers)


@get('/get_messages')
def get_messages():
	return json.dumps(messages[0:2])


@route('/')
@view('index')
def index():
	return {'messages': messages[0:2]}

   
@route('/', method="POST")
def send():
    nick = request.forms.get('nick')
    msg = request.forms.get('message')
    if [nick, msg] not in messages:
		messages.append([nick, msg])
		#, dict({peer:clock})
    redirect('/')


def sync_msgs():
    time.sleep(10)
    while True:
        time.sleep(3)
        for p in peers:
            r = requests.get(p + '/get_messages')
            msgs = json.loads(r.text)
            for msg in msgs:
				if msg not in messages:
					messages.append(msg)


def sync_peers():
    time.sleep(5)
    while True:
        np = []
        time.sleep(5)
        for p in peers:
            r = requests.get(p + '/get_peers')
            np = np + json.loads(r.text)
        
        peers[:] = list(set(np + peers))
        print(peers)


#t = threading.Thread(target=sync_peers)
#t.start()
#t2 = threading.Thread(target=sync_msgs)
#t2.start()


clock = 0
run(host='localhost', port=int(sys.argv[1]))
