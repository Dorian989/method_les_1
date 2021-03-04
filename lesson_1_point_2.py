from pprint import pprint
import vk
import json

session = vk.Session(access_token="2c4ff30fb47a1efcba9293b4510457e865e0a25963c5032a7de5f0e7351a07654f5abef605eb7cefeb483")
vkapi = vk.API(session)
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}
r = vkapi.friends.get(v=5.21, headers=headers)

pprint(r)


with open("data_test.json", "w") as f:
     json.dump(r, f)