from django.shortcuts import render
from .models import Product
from django.conf import settings

import os
import json

# Create your views here.
def index(request):
    items = list()
    date = None

    path = os.path.join(settings.STATIC_ROOT, 'stores/cu.json')
    with open(path, 'r') as f:
        data = json.loads(f.read())
        items += data['items']
        date = data['date']

    path = os.path.join(settings.STATIC_ROOT, 'stores/gs25.json')
    with open(path, 'r') as f:
        data = json.loads(f.read())
        items += data['items']

    path = os.path.join(settings.STATIC_ROOT, 'stores/7eleven.json')
    with open(path, 'r') as f:
        data = json.loads(f.read())
        items += data['items']

    path = os.path.join(settings.STATIC_ROOT, 'stores/ministop.json')
    with open(path, 'r') as f:
        data = json.loads(f.read())
        items += data['items']


    # current_user = request.user
    # print(current_user)
    # social = current_user.social_auth.filter(provider='google_oauth2').get()
    # access_token = social.get_access_token(load_strategy())
    # print(access_token)


    return render(request, 'stores/index.html', { 'items': items, 'date': date})



def cu(request):
    items = []
    date = None

    path = os.path.join(settings.STATIC_ROOT, 'stores/cu.json')

    with open(path, 'r') as f:
        data = json.loads(f.read())
        items = data['items']
        date = data['date']

    return render(request, 'stores/index.html', { 'items': items, 'date': date })


def gs25(request):
    items = []
    date = None

    path = os.path.join(settings.STATIC_ROOT, 'stores/gs25.json')

    with open(path, 'r') as f:
        data = json.loads(f.read())
        items = data['items']
        date = data['date']

    return render(request, 'stores/index.html', { 'items': items, 'date': date })


def sel(request):
    items = []
    date = None

    path = os.path.join(settings.STATIC_ROOT, 'stores/7eleven.json')

    with open(path, 'r') as f:
        data = json.loads(f.read())
        items = data['items']
        date = data['date']

    return render(request, 'stores/index.html', { 'items': items, 'date': date })



def ministop(request):
    items = []
    date = None

    path = os.path.join(settings.STATIC_ROOT, 'stores/ministop.json')

    with open(path, 'r') as f:
        data = json.loads(f.read())
        items = data['items']
        date = data['date']

    # current_user = request.user
    # print(current_user)
    # social = current_user.social_auth.filter(provider='google_oauth2').get()
    # access_token = social.get_access_token(load_strategy())
    # print(access_token)
    return render(request, 'stores/index.html', { 'items': items, 'date': date })
