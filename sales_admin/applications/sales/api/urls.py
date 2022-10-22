from rest_framework import routers
from applications.sales.api.views import OrderViewSet, OrderItemViewSet, GetOrderWithToken, CustomerViewSet, GainViewSet
from django.urls import path
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('orders', OrderViewSet)
router.register('order-items', OrderItemViewSet)
router.register('customers', CustomerViewSet)
router.register('gains', GainViewSet)


urlpatterns = [
    path("", include(router.urls), name="api-sales"),
    path("order/<int:id>/", GetOrderWithToken.as_view(), name='get-order-token')
]
