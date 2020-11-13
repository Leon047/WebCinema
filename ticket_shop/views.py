from django.shortcuts import render
from django.views.generic import ListView, View

from .models import MovieDescription


class HomePageList(ListView):
    model = MovieDescription
    queryset = MovieDescription.objects.all()
    template_name= 'ticket_shop/home_page.html'


class BuyingTicketPage(View):

    def get(self, request, title):
        item = MovieDescription.objects.get(title__iexact=title)
        return render(request, 'ticket_shop/buying_ticket_page.html', {'item': item})
