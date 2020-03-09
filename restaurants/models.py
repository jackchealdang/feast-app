from django.db import models

from django.test import TestCase
import requests
import json

API_KEY = '5QkhJ9hLlixw7cPGPg1cENNNeYN90xvHcF_7S2clOJqjvJ2Nd666TEe-WwwlXl0yriRMqcqXAchrgAkW0bZZwz1ZHTHffhgzwdz--yQLZmJDn7-7gmJtL-rpJM9cXnYx'
USER_AGENT = 'a6cLJRug_TnhY2FF6X2iHA'

# Create your models here.

class Restaurant(models.Model):
    name = ''
    location = ''

    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image_url = models.CharField(max_length=2300)
    display_phone = models.CharField(max_length=255, default ='')
    price = models.CharField(max_length=10, default ='')
    rating = models.CharField(max_length=10, default ='')
    search_url = models.CharField(max_length=2300, default ='')

    def __str__(self):
        """String for representing the Model object."""
        return self.name



def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def search():
    headers = {
        'Authorization': 'Bearer %s' % API_KEY,
    }

    limit = 5

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

