from django.test import TestCase
import requests
import json

# Create your tests here.

parameters = {
    "lat": 40.71,
    "lon": -74
}


response = requests.get("http://api.open-notify.org/iss-pass.json", params = parameters)
# print(response.status_code)
# print(response.json())

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# jprint(response.json())

pass_times = response.json()['response']
# jprint(pass_times)


# extract 5 risetime values

risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

# print(risetimes)

from datetime import datetime
times = []
for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    # print(time)

# ---------------------------------------------------------------------------------

API_KEY = '5QkhJ9hLlixw7cPGPg1cENNNeYN90xvHcF_7S2clOJqjvJ2Nd666TEe-WwwlXl0yriRMqcqXAchrgAkW0bZZwz1ZHTHffhgzwdz--yQLZmJDn7-7gmJtL-rpJM9cXnYx'
USER_AGENT = 'a6cLJRug_TnhY2FF6X2iHA'

headers = {
        'Authorization': 'Bearer %s' % API_KEY,
    }

# response = requests.get('https://api.yelp.com/v3/businesses/WavvLdfdP6g8aZTtbBQHTw', headers=headers)
# jprint(response.json())


limit = 5;

url_params = {
    'term': 'sushi',
    'location': 'Texas',
    'limit': limit,
}

r = requests.get('https://api.yelp.com/v3/businesses/search', headers=headers, params=url_params)
# jprint(r.json())
# jprint(r.json()['businesses'][0]['categories'][1]['alias'])


for n in range(limit):
    jprint(r.json()['businesses'][n-1]['name'])
    jprint(r.json()['businesses'][n-1]['location']['address1'])
    jprint(r.json()['businesses'][n-1]['coordinates'])
    print('\n')