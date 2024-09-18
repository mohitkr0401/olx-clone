from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def product(request):
    return render(request, 'products/products.html')
