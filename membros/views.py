from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "index.html")

def ajuda(request):
    return render(request, "ajuda.html")

