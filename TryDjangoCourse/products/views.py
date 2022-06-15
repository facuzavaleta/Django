from webbrowser import get
from django.shortcuts import get_object_or_404, redirect, render
from django.template import context
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.

def dynamic_lookup_view(request, id):
    obj = Product.objects.get(id=id)
    context = {
        "object" : obj
    }
    return render(request, "products/product_detail.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form' : form
    }
    return render(request, "products/product_create.html", context)

def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request, "products/product_create.html", context)

def product_detail_view(request):
    obj = get_object_or_404(Product, id=id)
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404 (Product, id=id)
    if request.method is "POST":
        obj.delete()
        return redirect ('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)

def product_list_view(request):
    queryset= Product.objects.all()
    context= {
        "object_list" : queryset
    }
    return render(request, "products/product_list.html", context)