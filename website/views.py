from django.shortcuts import render


def home(request):

    return render(request, "home.html", {})


def add(request):

    return render(request, "add.html", {})


def search(request):

    return render(request, "search.html", {})