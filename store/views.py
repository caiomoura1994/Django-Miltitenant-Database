from rest_framework import mixins, viewsets

from store.models import Address, Category, OpeningHour, Product, Store
from store.serializers import (AddressSerializer, CategorySerializer,
                               OpeningHourSerializer, ProductSerializer,
                               StoreSerializer)


class AddressViewSet(mixins.UpdateModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    class Meta:
        model = Address


class StoreViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    lookup_field = "slug"

    class Meta:
        model = Store


class OpeningHourViewSet(mixins.UpdateModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = OpeningHour.objects.all()
    serializer_class = OpeningHourSerializer

    class Meta:
        model = OpeningHour


class ProductViewSet(mixins.UpdateModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    class Meta:
        model = Product


class CategoryViewSet(mixins.UpdateModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    class Meta:
        model = Category
