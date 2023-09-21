#libraries and modules

import math
import random
import requests

num_float = 23.66

print(math.ceil(num_float))

rand_list = [1,2,3,4,5,6]
print(random.choice(rand_list))

rand_num = random.randint(1,10)
print(rand_num)

requests_bbc = requests.get("https://www.bbc.co.uk/")
print(requests_bbc.content)