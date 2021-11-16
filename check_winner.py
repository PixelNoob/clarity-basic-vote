import requests as r
import json
import time

headers = {'content-type': 'application/json'}

# call a read-only function

data = json.dumps({
  "sender": "ST3284BM8F1PSK0V7F1C1KTV9GXMFVMG4E7Z701RM",
  "arguments": [
  ]
})
url = 'https://stacks-node-api.testnet.stacks.co/v2/contracts/call-read/ST113MYNN52BC76GWP8P9PYFEP7XWJP6S5YFQM4ZE/simple-vote-2/get-{}'

c1 = r.post(url.format('candidate1'), data=data, headers=headers).json()
c2 = r.post(url.format('candidate2'), data=data, headers=headers).json()

c1 = (int(float.fromhex(c1['result'][20:36])))
c2 = (int(float.fromhex(c2['result'][20:36])))

print('Candidate 1: {} votes'.format(c1))
print('Candidate 2: {} votes'.format(c2))

def winner(c1,c2):
    if c1 > c2:
        return 1
    elif c2 > c1:
        return 2
    else:
        return 0

winner = winner(c1,c2)

if winner != 0:
    print('Candidate {} is winning'.format(winner))
