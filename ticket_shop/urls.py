"""WebCinema URL Configuration"""
from django.urls import path

from .views import HomePageList, BuyingTicketPage

urlpatterns = [
    path('', HomePageList.as_view(), name='home_page_url'),
    path('buying_ticket_page/<str:title>/', BuyingTicketPage.as_view(),
         name='buying_ticket_page_url'),
]
