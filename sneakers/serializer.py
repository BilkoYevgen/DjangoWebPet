from rest_framework import serializers
from .models import Product, ProdImage


class ProdImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdImage
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    images = ProdImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'