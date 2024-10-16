from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'appDANCE/index.html')
def dance(request):
    return render(request, 'appDANCE/dance.html')

def about(request):
    return render(request, 'appDANCE/about.html')
