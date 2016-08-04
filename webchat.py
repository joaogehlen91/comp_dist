from bottle import route, run, template, request, redirect, view, BaseResponse, BaseRequest, response

messages = [('Admin', 'Welcome')]

@route('/')
@view('index')
def index():
    return {'messages': messages}
 #   nick = request.get_cookie('nick')
 #   if not nick:
 #       redirect('/login')
    
 #   response.set_cookie('nick', 'joao')
    
    

    
@route('/', method="POST")
def send():
    nick = request.forms.get('nick')
    msg = request.forms.get('message')
    messages.append((nick, msg))
    redirect('/')


#@route('/login', method='POST')
#@view('login')
#def login():
#    pass

run(host='localhost', port=8080)