from django.urls import path
from.import views

urlspatterns =[
   # path('' ,views.prouducts_list, name='prouduct_list'),
    path('prouducts/',views.ProductListCreateview.as_view(), name='product-detail'),
    
]