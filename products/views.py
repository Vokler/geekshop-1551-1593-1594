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


def test_context(request):
    context = {
        'title': 'GeekShop - Тестовый контекст',
        'header': 'Welcome!',
        'username': 'Иван Иванов',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090},
            {'name': 'Синяя куртка The North Face', 'price': 23725},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390},
        ],
        'is_promotion': False,
    }
    return render(request, 'products/test-context.html', context)
