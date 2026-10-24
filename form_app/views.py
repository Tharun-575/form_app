
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from django.db.models import Q

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'product_form.html', {'form': form})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def search_product(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query) if query else Product.objects.none()

    return render(request, 'productsearch.html', {
        'products': products,
        'query': query
    })
