from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Category, Item

def index(request):
    context = {}
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()


    context = {
        'categories': categories,
        'items': items
        }
    return render(request, 'core/index.html', context)

def contact(request):
    context = {}
    return render(request, 'core/contact.html')

def detail(request, pk): # card details
    item = get_object_or_404(Item, pk=pk)
    context = {'item': item}
    return render(request, 'item/detail.html', context)