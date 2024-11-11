from django.shortcuts import render



def home_page(request):
    return render(request, 'third_task/platform.html')


def shop_page(request):
    context = {
        'Товар1': '500 рублей',
        'Товар2': '700 рублей',
        'Товар3': '300 рублей',
    }

    return render(request, 'third_task/product.html', {'context': context})


def cart_page(request):
    return render(request, 'third_task/cart.html')
