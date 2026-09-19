# отвечает за методы, которые будут вызваны при переходу пользователя на какую-то страницу
from django.shortcuts import render
from .models import MenuDish


# Create your views here.
def menu(request):

    hot = MenuDish.objects.filter(category="hot")
    cold = MenuDish.objects.filter(category="cold")
    drinks = MenuDish.objects.filter(category="drinks")

    context = {
        'hot': hot,
        'cold': cold,
        'drinks': drinks



    }

    return render(request, 'menu/menu.html', context)


