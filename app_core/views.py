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
            id = product['id']
            title = product['title']
            description = product['description']
            price = product['price']
            image = product['images'][0]
            
            products.append({
                'id': id,
                'title': title,
                'description': description,
                'price': price,
                'image': image
            })
    else:
        print("Nie udało się pobrać danych produktów")
            
    
    return render(request, 'home.html', {'products': products})

def product(request, pk):
    # response = requests.get("http://fakestoreapi.com/products/{}".format(id))
    # product = response.json()
    response = requests.get(f"https://dummyjson.com/products/{pk}")
    product = response.json()
    
    return render(request, 'product.html', {'product': product})