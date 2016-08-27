import requests
import json

messages = []
clock = 0
peer = 8081

r = requests.get('http://localhost:8080/get_messages')
msgs = json.loads(r.text)

print(msgs)

for msg in msgs:
    if msg not in messages:
        clock += 1
        d = dict(msg[2])
        d.update({peer:clock})
        messages.append([msg[0], msg[1], d])


print(messages)