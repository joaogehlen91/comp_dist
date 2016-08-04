from bottle import route, run, template, request, redirect, view, BaseResponse, BaseRequest, response

messages = [('Admin', 'Welcome')]

#@get('/peers')
#def peers():
	#return peers

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
