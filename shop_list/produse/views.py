from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Products
from .forms import ProductsForm

# products = [
#     {
#         'id': 1,
#         'nume': 'paine',
#         'cumparat': True
#     },
#     {
#         'id': 2,
#         'nume': 'oua',
#         'cumparat': False
#     },
#     {
#         'id': 3,
#         'nume': 'lapte',
#         'cumparat': False
#     }
# ]

def home(request):
    # return HttpResponse('<h2>Lista Produse</h2>')
    if request.method == 'POST':
        form= ProductsForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = ProductsForm()
            products = Products.objects.all()
            context = {'form': form, 'products':products}
            return render(request, 'produse/home.html',context)
    else:
        form= ProductsForm()
        products = Products.objects.all()
        context = {'form': form, 'products': products}
        return render(request, 'produse/home.html', context)

def delete(request, id):
    product = Products.objects.get(pk=id)
    product.delete()
    return redirect('home')

def change_status(request, id):
    product = Products.objects.get(pk=id)
    if product.cumparat:
        product.cumparat = False
        product.save()
    else:
        product.cumparat = True
        product.save()

    return redirect('home')

def about(request):
    # return HttpResponse('<h2>About my app</h2>')
    return render(request, 'produse/about.html')