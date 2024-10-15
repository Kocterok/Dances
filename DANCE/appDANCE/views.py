from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the appDANCE index.")
    # return render(request, 'appDANCE/index.html')
def dance(request):
    return HttpResponse("<H4/>Hello, dances<H4/>")
