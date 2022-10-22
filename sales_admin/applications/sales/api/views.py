from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from applications.sales.models import Order, OrderItem, Customer
from applications.sales.api.serializers import OrderSerializer, OrderItemSerializer, CustomerSerializer, GainSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class OrderViewSet(ModelViewSet):
    """
    Clase ViewSet de Order
    """

    # Obtenemos los datos que queremos devolver
    queryset = Order.objects.all()

    # Le indicamos el serializer que debe utilizar para convertir los objetos a JSON
    serializer_class = OrderSerializer

    # Configuracion para que el VIEW sea utilizado por usuarios autenticados
    # permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['number', 'date', 'delivery_date', 'total']

    Ordering_fields = ['date']


class GetOrderWithToken(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None, id=0, *args, **kwargs):
        order = None

        req_user = request._user
        have_permission = False
        if req_user.has_perm('sales.view_order'):
            have_permission = True
            try:
                order = Order.objects.get(id=id)
            except order.DoesNotExist:
                pass

        order_serializer = OrderSerializer(
            order
        )

        payload = {
            'order': order_serializer.data,
            'have_permission': have_permission
        }

        return JsonResponse(payload)


class OrderItemViewSet(ModelViewSet):
    """
    Clase ViewSet de OrderItem
    """

    # Obtenemos los datos que queremos devolver
    queryset = OrderItem.objects.all()

    # Le indicamos el serializer que debe utilizar para convertir los objetos a JSON
    serializer_class = OrderItemSerializer

    # Configuracion para que el VIEW sea utilizado por usuarios autenticados
    # permission_classes = [IsAuthenticated]


class CustomerViewSet(ModelViewSet):
    """
    Clase ViewSet de Customer
    """

    # Obtenemos los datos que queremos devolver
    queryset = Customer.objects.all()

    # Le indicamos el serializer que debe utilizar para convertir los objetos a JSON
    serializer_class = CustomerSerializer

    # Configuracion para que el VIEW sea utilizado por usuarios autenticados
    # permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['ruc', 'category']

    Ordering_fields = ['id']


class GainViewSet(ModelViewSet):
    """
    Clase ViewSet de Customer
    """
    # Obtenemos los datos que queremos devolver
    queryset = Order.objects.all()

    # Le indicamos el serializer que debe utilizar para convertir los objetos a JSON
    serializer_class = GainSerializer

    # Configuracion para que el VIEW sea utilizado por usuarios autenticados
    # permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['number']

    Ordering_fields = ['date']
