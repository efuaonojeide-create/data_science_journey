'''
import requests

r = requests.get('https://api.github.com', params=b"q:language:python&sort:stars&order:desc")

r_dict = r.json()

print (r.headers)
'''

#Thursday Warmup
'''
import requests

r = requests.get('https://jsonplaceholder.typicode.com/users/1')

r_dict = r.json()

print(r_dict)
'''
#Thursday's Core
'''
import requests

r = requests.get('https://jsonplaceholder.typicode.com/users/1')

r_dict = r.json()

print (r_dict['name'])
print (r_dict[('email')])
'''
#Thursday's Challenge

import requests

r = requests.get('https://jsonplaceholder.typicode.com/users')

r_dict = r.json()

for user in r_dict:
    city = user['address']['city']
    if 'a' in city:
        print (user['name'])