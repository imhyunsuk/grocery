from django.shortcuts import render
from .models import Product
from django.conf import settings
import os
import json

# Create your views here.
def index(request):
    products = Product.objects.all()
    path = os.path.join(settings.STATIC_ROOT, 'stores/cu.json')

    items = []
    date = None
    with open(path, 'r') as f:
        data = json.loads(f.read())
        items = data['items']
        date = data['date']
    # current_user = request.user
    # print(current_user)
    # social = current_user.social_auth.filter(provider='google_oauth2').get()
    # access_token = social.get_access_token(load_strategy())
    # print(access_token)
    return render(request, 'stores/index.html', { 'items': items, 'date': date})



def cu(request):
    path = os.path.join(settings.STATIC_ROOT, 'stores/cu.json')

    items = []
    with open(path, 'r') as f:
        d1 = json.loads(f.read())
        items = d1['items']
    # current_user = request.user
    # print(current_user)
    # social = current_user.social_auth.filter(provider='google_oauth2').get()
    # access_token = social.get_access_token(load_strategy())
    # print(access_token)
    return render(request, 'stores/cu.html', { 'items': items })


def gs25(request):
    path = os.path.join(settings.STATIC_ROOT, 'stores/cu_201812.json')

    items = []
    with open(path, 'r') as f:
        d1 = json.loads(f.read())
        items = d1['items']
    # current_user = request.user
    # print(current_user)
    # social = current_user.social_auth.filter(provider='google_oauth2').get()
    # access_token = social.get_access_token(load_strategy())
    # print(access_token)
    return render(request, 'stores/gs25.html', { 'items': items })


def sel(request):
    path = os.path.join(settings.STATIC_ROOT, 'stores/7eleven.json')

    items = []
    with open(path, 'r') as f:
        d1 = json.loads(f.read())
        items = d1['items']
    # current_user = request.user
    # print(current_user)
    # social = current_user.social_auth.filter(provider='google_oauth2').get()
    # access_token = social.get_access_token(load_strategy())
    # print(access_token)
    return render(request, 'stores/7eleven.html', { 'items': items })



def ministop(request):
    path = os.path.join(settings.STATIC_ROOT, 'stores/ministop.json')

    items = []
    with open(path, 'r') as f:
        d1 = json.loads(f.read())
        items = d1['items']
    # current_user = request.user
    # print(current_user)
    # social = current_user.social_auth.filter(provider='google_oauth2').get()
    # access_token = social.get_access_token(load_strategy())
    # print(access_token)
    return render(request, 'stores/ministop.html', { 'items': items })
