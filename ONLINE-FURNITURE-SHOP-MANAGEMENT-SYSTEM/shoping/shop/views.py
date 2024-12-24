from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

def home(request):
    return render(request,"shop/index.html")

def register(request):
    return render(request,"shop/register.html")

def collections(request):
    categories = Category.objects.all() 
    return render(request, 'shop/collections.html', {'category': categories})


def collectionsview(request, name):
    category = get_object_or_404(Category, name=name, status=0) 
    products = product.objects.filter(Catagory=category)
    
    if products.exists():
        return render(request, 'shop/products/index.html', {'category': category, 'products': products})
    else:
        messages.warning(request, 'No products found in this category.')
        return redirect('collections') 
def product_details(request , cname, pname):
    if Category.objects.filter(name=cname, status=0):
        if product.objects.filter(name=pname, status=0): 
            products = product.objects.filter(name=pname, status=0).first() 
            return render(request, 'shop/products/product_details.html', {'products': products})
        else:
            messages.error(request, 'Product not found')
            return redirect('collections')
    else:
        messages.error(request, 'No Such category found')
        return redirect('collections')  
