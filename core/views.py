from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Category, Item

from .forms import SignupForm

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
    return render(request, 'core/contact.html', context)

def signup(request):
    form = SignupForm()
    
    return render(request, 'core/signup.html', {
            'form': form
        })

def detail(request, pk): # card details
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)
    # print(related_items)


    context = {'item': item,
               'related_items': related_items}
    return render(request, 'core/detail.html', context)