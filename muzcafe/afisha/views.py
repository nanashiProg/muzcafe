from django.shortcuts import render
from .models import Posters

def afisha(request):

    posters = Posters.objects.order_by('date')

    return render(request, 'afisha/afisha.html', {'posters': posters})
