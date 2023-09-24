import json

import requests

post_codes_req = requests.get("https://api.postcodes.io/postcodes/e149ae")

'''print(post_codes_req) #200
print(post_codes_req.headers) #gives the headers
print(post_codes_req.content) # gives json body as bytes

post_codes_dict = json.loads(post_codes_req.content) #turn into python
print(type(post_codes_req))'''