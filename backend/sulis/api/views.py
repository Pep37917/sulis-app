from rest_framework.viewsets import ModelViewSet
from ..models import Bin
from .serializers import BinSerializer

class BinViewSet(ModelViewSet):
    queryset = Bin.objects.all()
    serializer_class =  BinSerializer