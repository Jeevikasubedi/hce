from django.shortcuts import render
from prouducts.models import Products
from.models import Category
def categories_list(request):
    categories=Category.objects.all()
    return render(request,'categories/categories_list.html',{'categories':categories})
def category_prouducts(request):
    categories= Category.objects.all()
    prouducts=Products.objects.all()
    return render(request,'categories/categories_prouducts.html',{'categories':categories, 'prouducts':prouducts})

# Create your views here.
