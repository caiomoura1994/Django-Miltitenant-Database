from rest_framework import serializers

from store.models import Address, Category, OpeningHour, Product, Store


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


class StoreSerializer(serializers.ModelSerializer):
    # categories = CategorySerializer(many=True, read_only=True)
    products = ProductSerializer(many=True, read_only=True)
    address = AddressSerializer(read_only=True)
    openinghours = OpeningHourSerializer(many=True, read_only=True)

    class Meta:
        model = Store
        exclude = ('profile', )
