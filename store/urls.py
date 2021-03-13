from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from store.views import (AddressViewSet, CategoryViewSet, OpeningHourViewSet,
                         ProductViewSet, StoreViewSet)

router = routers.DefaultRouter()
router.register(r'address', AddressViewSet)
router.register(r'store', StoreViewSet)
router.register(r'opening-hour', OpeningHourViewSet)
router.register(r'product', ProductViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
