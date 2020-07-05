from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

def index(request):
    # products=Product.objects.all()
    # n=len(products)
    
    # n_slides=(n//4)+ceil((n/4)-(n//4))
    # allprods=[[products, range(1, n_slides), n_slides],
    #           [products, range(1, n_slides), n_slides]]
    # params={"allprods": allprods}
    #print(n_slides)
    #params= {'product' : products , 'slides' : n_slides , 'range' : range(1,n_slides)}

    allprods = []
    catprods = Product.objects.values('product_category')
     
    
    cats=[]
    for i in catprods:
        if(i['product_category'] not in cats):
            cats.append(i['product_category'])
    
    # cats = {item['product_category'] for item in catprods}
    
    for cat in cats:
        prod = Product.objects.filter(product_category=cat)
        
        n = len(prod)
        n_Slides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, n_Slides), n_Slides])
    params = {'allprods':allprods}

    return render(request, 'shop/index.html', params)
def about(request):
    return render(request, 'shop/about.html')
def tracking(request):
    return render(request, 'shop/tracking.html')
def search(request):
    return render(request, 'shop/search.html')
def contacts(request):
     
    return render(request, 'shop/contacts.html')
def checkout(request):
     
    return render(request, 'shop/checkout.html')
def products(request, my_id):
    products=Product.objects.filter(id=my_id)
    # print(products)
    params_products={'products' : products[0]}
    return render(request, 'shop/products.html', params_products)