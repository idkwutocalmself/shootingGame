from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def main_page(request):
    return render(request, 'main_page.html')

def singleplayer(request):
    return render(request, 'singleplayer.html')

def multiplayer(request):
    return render(request, 'multiplayer.html')