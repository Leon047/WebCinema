"""WebCinema URL Configuration"""
from django.urls import path

from .views import *

urlpatterns = [
    path('', home_page, name='home_page_url'),
    path('buying_ticket_page/<str:title>/', buying_ticket_page, name='buying_ticket_page_url'),
]
