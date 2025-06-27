from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.template import loader
from .models import Item
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ItemForm, UserRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return render(request, 'index.html')


def base(request):
    return render(request, 'base.html')


@login_required
def inventory_list(request):
    items = Item.objects.all()  
    return render(request, "inventory_list.html", {'inventory_items': items})


@login_required
def inventory_create(request):
    print("POST data:", request.POST)
    if request.method == 'POST':
        form = ItemForm(request.POST) 
        if form.is_valid():
            form.save()  
            return redirect(reverse('inventory_list'))  
    else:
        form = ItemForm() 
    return render(request, 'inventory_form.html', {'form': form, 'action': 'Create'})


@login_required
def inventory_detail(request, id):
    item = get_object_or_404(Item, pk=id)  
    return render(request, 'inventory_detail.html', {'inventory_item': item})


@login_required
def inventory_update(request, pk):
    
    item = get_object_or_404(Item, pk=pk)  
    print(item)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item) 
        if form.is_valid():
            form.save() 
            return redirect(reverse('inventory_list')) 
    else:
        form = ItemForm(instance=item)  
    return render(request, 'inventory_form.html', {'form': form, 'action': 'Edit', 'inventory_item': item})  

@login_required
def edit_inventory(request, pk):
    item = get_object_or_404(Item, pk=pk)
    
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventory_detail', id=item.pk) 
        else:
            print(form.errors) 
    else:
        form = ItemForm(instance=item)
    return render(request, 'inventory_form.html', {
        'form': form,
        'action': 'Edit',
        'inventory_item': item
    })



@login_required
def inventory_delete(request, pk):
   
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect(reverse('inventory_list'))
    return render(request, 'inventory_confirm_delete.html', {'inventory_item': item})  # GET request


def register(request):    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)  
        if form.is_valid():
            form.save() 
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login') 
        else:
            context = {'form': form}
            return render(request, 'register.html', context)
    else:
        form = UserRegistrationForm()  
    context = {'form': form}
    return render(request, 'register.html', context)



def my_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('base')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()   
    return render(request, 'login.html', {'form': form}) 

