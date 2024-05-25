from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.filters import SearchFilter
from .models import Prouducts
from .serializers import productserializer

def prouducts_list(request):
    Prouducts = Prouducts.objects.all()
    return render(request,'products/product_list.html' ,{'prouducts':Prouducts})
class productListcreateview(generics.ListcreateAPIView):
    queryset =Prouducts.objects.all()
    serializer_class = productserializer
    filter_backends =[SearchFilter]
    search_fields =['name' ,'description']

    class productRetrieveUpdateDestroyView(generics.RetrieveDestroyAPIView):
        queryset = Prouducts.objects.all()
        serializer_class =productserializer       
                 
