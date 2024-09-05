from django.shortcuts import render
import requests

def home(request):
    response = requests.get("https://fakestoreapi.com/products?limit=20")
    products = response.json()
    print(products[0])
    
    return render(request, 'home.html', {'products': products})

def product(request, id):
    response = requests.get("http://fakestoreapi.com/products/{}".format(id))
    product = response.json()
    
    return render(request, 'product.html', {'product': product})