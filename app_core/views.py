from django.shortcuts import render
import requests

def home(request):
    # response = requests.get("https://fakestoreapi.com/products?limit=20")
    # products = response.json()
    # response = requests.get("https://api.escuelajs.co/api/v1/products")
    # products = response.json()
    response = requests.get("https://dummyjson.com/products")
    data = response.json()

    products = []
    if 'products' in data:
        for product in data['products']:
            title = product['title']
            description = product['description']
            price = product['price']
            image = product['images'][0]
            
            products.append({
                'title': title,
                'description': description,
                'price': price,
                'image': image
            })
    else:
        print("Nie udało się pobrać danych produktów")
            
    
    return render(request, 'home.html', {'products': products})

def product(request, id):
    # response = requests.get("http://fakestoreapi.com/products/{}".format(id))
    # product = response.json()
    
    return render(request, 'product.html', {'product': product})