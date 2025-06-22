from django.shortcuts import render, redirect
from .models import IceCream
from .forms import IceCreamForm

def home(request):
    items = IceCream.objects.all()
    return render(request, 'inventory/home.html', {'items': items})

def add_ice_cream(request):
    if request.method == 'POST':
        form = IceCreamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IceCreamForm()
    return render(request, 'inventory/add.html', {'form': form})
