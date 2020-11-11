from django.shortcuts import render
# from django.views.generic import ListView

from .models import MovieDescription


# class HomeList(ListView):
#     queryset = MovieDescription.objects.all()
#     template_name = 'ticket_shop/home_page.html'

def home_page(request):
    item_list = MovieDescription.objects.all()
    return render(request, 'ticket_shop/home_page.html', {'item_list': item_list})

def buying_ticket_page(request, title):
    item = MovieDescription.objects.get(title__iexact=title)
    return render(request, 'ticket_shop/buying_ticket_page.html', {'item': item})
