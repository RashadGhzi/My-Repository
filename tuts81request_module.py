import json

import requests
import json
r = requests.get("https://www.facebook.com/").text
# print(r.text)
# print(r.status_code)
# print(type(r.status_code))
# print(type(r))
# print(type(r.text))
r1 = json.loads(r)
print(type(r1))


# url = ("www.something.com")
# data = {
#     "p1": 20,
#     "p2": 620
# }
#
# r2 = requests.post(url=url,data=data)