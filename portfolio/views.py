

# Create your views here.
from django.shortcuts import render
from .models import Project

def portfolio(request):
    
    return render(request, 'portfolio/index.html')
