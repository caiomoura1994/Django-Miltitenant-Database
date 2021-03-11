from rest_framework import serializers

from store.models import Address, Category, OpeningHour, Product, Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        exclude = ('profile', )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class OpeningHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHour
        fields = '__all__'
