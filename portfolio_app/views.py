from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request: object) -> HttpResponse:
    
    return render(request, 'portfolio_app/index.html')
    