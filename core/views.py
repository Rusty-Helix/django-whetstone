from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from .models import Category, Item

from .forms import SignupForm, NewItemForm

from django.contrib.auth.decorators import login_required

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
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
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

@login_required
def new(request):
    if request.method == 'POST':
        form=NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.creator = request.user
            item.save()

            return redirect('detail', pk=item.id)
    else:
        form = NewItemForm()

    form = NewItemForm()

    context = {'form': form,
               'title': 'New Item' }
    return render(request,
                  'core/newItemForm.html',
                  context)
