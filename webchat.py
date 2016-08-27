from bottle import route, run, request, redirect, view, get
import json
import sys
import time
import requests
import threading

messages = []
clock = 1
peers = sys.argv[2:]
peer = sys.argv[1]

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
    global clock
    nick = request.forms.get('nick')
    msg = request.forms.get('message')
    if [nick, msg] not in messages:
        messages.append([nick, msg, {peer:clock}])
        clock += 1
    redirect('/')


def sync_msgs():
    time.sleep(10)
    global clock
    while True:
        time.sleep(3)
        for p in peers:
            r = requests.get(p + '/get_messages')
            msgs = json.loads(r.text)
            for msg in msgs:
                if msg not in messages:
                    clock += 1
                    d = dict(msg[2])
                    d.update({peer:clock})
                    messages.append([msg[0], msg[1], d])
                    #pensar em alguma forma de atualizar dict quando recebe mensagem de outro server


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
