from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from users.models import Payments
from users.serializers import PaymentsSerializer


# Create your views here.
class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['paid_course', 'payment_method']
    ordering_fields = ['data_of_payment']
