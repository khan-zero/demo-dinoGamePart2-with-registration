from django.shortcuts import render

def index(request):
    return render(request, 'dino2/index.html')
