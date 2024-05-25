from rest_framework import serializers
from .models import Products

class productserializer(serializers.ModelSerializer):
    class meta:
        model = Products
        fields = '__all__'
