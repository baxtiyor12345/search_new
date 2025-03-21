from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('index/', index, name='home'),
    path('category/<int:category_id>/', category_news),
    path('add_news/', add_news, name='add_news'),
    path('search/', search_view, name='search'),
    path('', login_view, name='login')


]
