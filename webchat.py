from bottle import route, run, template, request, redirect

messages = ['oi']


@route('/')
def index():
    return str(messages)


@route('/new')
def new():
    return '''
        <form action="/new" method="post">
            Message: <input name="message" type="text" />
            
            <input value="Enviar" type="submit" />
        </form>
    '''
    
@route('/new', method="POST")
def send():
    msg = request.forms.get('message')
    messages.append(msg)
    redirect('/')
    return str(msg)





run(host='localhost', port=8080)