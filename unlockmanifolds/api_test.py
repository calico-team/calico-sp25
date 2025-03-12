import io
import requests
import main
import json

import sys

USER = (sys.argv[1], sys.argv[2])
BASE_URL = 'https://calicojudge.com'
# r = requests.get(BASE_URL + '/api/v4/contests/3/problems', auth=USER)
# r = requests.get(BASE_URL + '/api/v4/status', auth=USER)
# print(r.text)

# problem_json = json.dumps([main.p.default_metadata('main')])
# print(problem_json)
# r = requests.post(BASE_URL + '/api/v4/contests/3/problems/add-data',
#                   files={'data': problem_json}, auth=USER)
# print(r.text)

# r = requests.post(BASE_URL + '/api/v4/contests/3/problems',
#                   # data={'problem': 692},
#                   files={'zip': open('unlockmanifolds_main.zip', 'rb')},
#                   auth=USER)
# print(r.text)

r = requests.post(BASE_URL + '/api/v4/problems',
                  data={'problem': 694},
                  files={'zip': open('unlockmanifolds_main.zip', 'rb')},
                  auth=USER)
print(r.text)
print(r.request)
print(r.content)

print(r.status_code)
