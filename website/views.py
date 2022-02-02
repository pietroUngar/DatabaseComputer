from django.shortcuts import render
from .forms import ComputerForm
from .models import Computer

def home(request):

    return render(request, "home.html", {})


def add(request):

    form = ComputerForm()
    return render(request, "add.html", {

        "form": form

    })


def search(request):

    elements = Computer.objects.all()
    return render(request, "search.html", {

        "elements": elements

    })