from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import NewsForm, SearchForm, UserLoginForm
from .models import *


def index(request):
    news = News.objects.all()
    cat = Categories.objects.all()
    context = {
        "categories": cat,
        "news": news,
        "title": "News title"
    }

    return render(request, "test.html", context=context)


def category_news(request, category_id):
    news = News.objects.filter(category_id=category_id)
    cat = Categories.objects.all()
    context = {
        "categories": cat,
        "news": news,
        "title": "News title"
    }

    return render(request, "index.html", context=context)


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = News.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = NewsForm()
    return render(request, 'add_news.html', {'form': form})


# def add_news(request):
#     if request.method=='POST':
#         form=NewsForm(request.POST)
#         if form.is_valid():
#             new=form.save()
#             return redirect(new)
#     else:
#         form = NewsForm()
#     return render(request, 'add_news.html', {'form': form})


class Post:
    pass


def search_view(request):
    query = ""
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = News.objects.filter(title__icontains=query)  # Sarlavha bo‘yicha qidirish
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form, 'results': results, 'query': query})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
    else:
      form = UserLoginForm()
    return render(request, 'login.html', {"form": form})
