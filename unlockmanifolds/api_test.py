import io
import requests
import main
import json

BASE_URL = 'https://calicojudge.com'
# r = requests.get(BASE_URL + '/api/v4/contests/3/problems', auth=('ejam', 'UaLgMZtr8PavGby'))
# r = requests.get(BASE_URL + '/api/v4/status', auth=('ejam', 'UaLgMZtr8PavGby'))
# print(r.text)

# problem_json = json.dumps([main.p.default_metadata('main')])
# print(problem_json)
# r = requests.post(BASE_URL + '/api/v4/contests/3/problems/add-data',
#                   files={'data': problem_json}, auth=('ejam', 'UaLgMZtr8PavGby'))
# print(r.text)

# r = requests.post(BASE_URL + '/api/v4/contests/3/problems',
#                   # data={'problem': 692},
#                   files={'zip': open('unlockmanifolds_main.zip', 'rb')},
#                   auth=('ejam', 'UaLgMZtr8PavGby'))
# print(r.text)

r = requests.post(BASE_URL + '/api/v4/problems',
                  # data={'problem': 692},
                  files={'zip': open('unlockmanifolds_main.zip', 'rb')},
                  auth=('ejam', 'UaLgMZtr8PavGby'))
print(r.text)

