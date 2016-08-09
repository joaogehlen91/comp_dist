from bottle import route, run, template, request, redirect, view, BaseResponse, BaseRequest, response, get
import json

messages = []

@get('/peers')
def peers():
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


run(host='localhost', port=8080)
