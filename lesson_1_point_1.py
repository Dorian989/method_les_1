import requests
import json
from pprint import pprint
url = "http://api.github.com/"
client_id = "c189f387deae14ad1e12"
client_secret = "0113697d3b364165aaf2a334116f1b0d7a85be23"
concret_params = {
    "client_id": client_id,
    "client_secret": client_secret
}
r = requests.post(url, params=concret_params)
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}
pprint(dict(r.headers))
print('done')
with open("data2.json", "w") as f:
    json.dump(r.json(), f)
