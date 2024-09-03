from django.shortcuts import render
import requests

def home(request):
    response = requests.get("https://fakestoreapi.com/products?limit=20")
    products = response.json()
    
    return render(request, 'home.html', {'products': products})