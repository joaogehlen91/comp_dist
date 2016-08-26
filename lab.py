import requests
import json

r = requests.get('http://localhost:8080/get_messages')
msgs = json.loads(r.text)

print(msgs)
