from bottle import route, run, template, request, redirect, view, BaseResponse, BaseRequest, response, get
import requests, json

messages = []


@route('/')
@view('index')
def index():
    data = requests.get('http://localhost:8080/peers')
    decoded = json.loads(data.text)
    for tupla in decoded: 
        messages.append(tupla)
    return {'messages': messages }
    
   
@route('/', method="POST")
def send():
    nick = request.forms.get('nick')
    msg = request.forms.get('message')
    messages.append((nick, msg))
    redirect('/')


run(host='localhost', port=7070)
