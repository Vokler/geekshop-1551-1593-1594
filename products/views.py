import json

from django.shortcuts import render
from django.conf import settings


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request):
    file_path = settings.BASE_DIR / 'products/fixtures/goods.json'
    context = {
        'title': 'GeekShop - Продукты',
        'products': json.load(open(file_path, encoding='utf-8'))
    }
    return render(request, 'products/products.html', context)
