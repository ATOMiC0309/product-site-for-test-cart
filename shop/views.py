from django.shortcuts import render, redirect
from .models import Product, Category
from .utils import CartAuthenticatedUser
from django.http import HttpResponse, HttpRequest


# Create your views here.

def index(request):
    context = {
        'products': Product.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'index.html', context=context)


def product_by_category(request, category_pk):
    category = Category.objects.get(pk=category_pk)
    context = {
        'products': Product.objects.filter(category=category),
        'categories': Category.objects.all()
    }
    return render(request, 'index.html', context=context)


def detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'detail.html', context={'product': product})


def cart(request):
    if request.user.is_authenticated:
        cart_info = CartAuthenticatedUser(request).get_cart_info()

        context = {
            'order_products': cart_info['order_products'],
            'cart_total_price': cart_info['cart_total_price'],
            'cart_total_quantity': cart_info['cart_total_quantity'],

        }
        return render(request, 'cart.html', context=context)
    else:
        return HttpResponse("Avval tizimga kiring!")


def to_cart(request: HttpRequest, product_id, action):
    if request.user.is_authenticated:
        CartAuthenticatedUser(request, product_id=product_id, action=action)
        page = request.META.get('HTTP_REFERER')
        return redirect(page)

    else:
        return HttpResponse("Avval tizimga kiring!")
