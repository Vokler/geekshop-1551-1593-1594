from django.shortcuts import render


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {'title': 'GeekShop - Продукты'}
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
