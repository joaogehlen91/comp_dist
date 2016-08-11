from bottle import route, run, request, redirect, view, get
import json
import sys
import time
import requests
import threading

messages = []
peers = sys.argv[2:]


@get('/get_peers')
def get_peers():
	return json.dumps(peers)


@get('/get_messages')
def get_messages():
	return json.dumps(messages)


@route('/')
@view('index')
def index():
    return {'messages': messages}
    
   
@route('/', method="POST")
def send():
    nick = request.forms.get('nick')
    msg = request.forms.get('message')
    messages.append((nick, msg))
    redirect('/')


def sync_msgs():
    time.sleep(6)
    while True:
        print('aqui')
        time.sleep(2)
        new_msgs = []
        for p in peers:
            r = requests.get(p + '/get_messages')
            new_msgs = new_msgs + json.loads(r.text)

        messages[:] = messages + new_msgs


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


t = threading.Thread(target=sync_peers)
t.start()
t2 = threading.Thread(target=sync_msgs)
t2.start()



run(host='localhost', port=int(sys.argv[1]))
