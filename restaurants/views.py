from django.http import HttpResponse
from django.shortcuts import render
from .models import Restaurant
import json, requests

import requests

API_KEY = '5QkhJ9hLlixw7cPGPg1cENNNeYN90xvHcF_7S2clOJqjvJ2Nd666TEe-WwwlXl0yriRMqcqXAchrgAkW0bZZwz1ZHTHffhgzwdz--yQLZmJDn7-7gmJtL-rpJM9cXnYx'
USER_AGENT = 'a6cLJRug_TnhY2FF6X2iHA'

# Create your views here.
def restaurants_index(request):
    headers = {
        'Authorization': 'Bearer %s' % API_KEY,
    }

    limit = 15

    url_params = {
        # 'location': location.replace(' ', '+'),
        'location': 'Texas',
        'limit': limit,
        'attributes': 'hot_and_new',
    }

    r = requests.get('https://api.yelp.com/v3/businesses/search', headers=headers, params=url_params)
    businesses = r.json().get('businesses')

    if not businesses:
        print(u'No businesses for {0} found.'.format(term))
        return render(request, 'results.html', {'text': 'No results found'})



    # text = r.json()['businesses'][0]['name']
    # jprint(r.json())

    rest = []

    for n in r.json()['businesses']:
        nme = n['name']
        loc = n['location']['address1']
        img = n['image_url']
        phn = n['display_phone']
        rtg = n['rating']
        # prc = n['price']
        sch = "https://www.google.com/maps/embed/v1/place?q=" + loc.replace(" ", "+") + "&key=AIzaSyBrJSAK_ei_3b0AW_tvOto-Kfg3cqXDl00"
        rest.append(Restaurant(name = nme, location = loc, image_url = img, display_phone=phn, rating=rtg, search_url=sch))


    total = r.json()['total']

    context = {
        'rest':rest,
        'total':total,
    }

    # return render(request, 'results.html', {'text':text})
    return render(request, 'restaurants_index.html', context=context)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


# def dinersButton(request, term, location=''):
def dinersButton(request):
    term = request.GET['search']

    headers = {
        'Authorization': 'Bearer %s' % API_KEY,
    }

    limit = 15

    url_params = {
        'term': term.replace(' ', '+'),
        # 'location': location.replace(' ', '+'),
        'location': 'Texas',
        'limit': limit,
    }

    r = requests.get('https://api.yelp.com/v3/businesses/search', headers=headers, params=url_params)
    businesses = r.json().get('businesses')

    if not businesses:
        print(u'No businesses for {0} found.'.format(term))
        return render(request, 'results.html', {'text': 'No results found'})



    text = r.json()['businesses'][0]['name']
    jprint(r.json())

    rest = []


    for n in r.json()['businesses']:
        nme = n['name']
        loc = n['location']['address1']
        img = n['image_url']
        phn = n['display_phone']
        rtg = n['rating']
        # prc = n['price']
        sch = "https://www.google.com/maps/embed/v1/place?q=" + loc.replace(" ", "+") + "&key=AIzaSyBrJSAK_ei_3b0AW_tvOto-Kfg3cqXDl00"
        rest.append(Restaurant(name = nme, location = loc, image_url = img, display_phone=phn, rating=rtg, search_url=sch))

        globalsearch_url = "https://www.google.com/maps/embed/v1/place?q=" + term + "&key=AIzaSyBrJSAK_ei_3b0AW_tvOto-Kfg3cqXDl00"

    total = r.json()['total']

    context = {
        'rest':rest,
        'total':total,
        'term':term,
        'globalsearch_url':globalsearch_url,
    }

    return render(request, 'results.html', context=context)

def maps(request):



    return render(request, 'maps.html')