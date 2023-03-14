from django.shortcuts import render
from .models import Prices, Portofolio

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def portofolio(request):
    portofolio = Portofolio.objects.all()
    context = {
        'portofolios': portofolio
    }
    return render(request, 'portofolio.html',context)

def products(request, pk):
    product = Prices.objects.get(id=pk)
    context = {
        'product': product
    }
    return render(request, 'products.html',context)

def price_list(request):
    price_list = Prices.objects.all()
    context = {
        'prices': price_list
    }
    return render(request, 'price_list.html',context)