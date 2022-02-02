from django.shortcuts import render
from .forms import ComputerForm

def home(request):

    return render(request, "home.html", {})


def add(request):

    form = ComputerForm()
    return render(request, "add.html", {

        "form": form

    })


def search(request):

    return render(request, "search.html", {})