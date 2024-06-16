from rest_framework.serializers import ModelSerializer
from ..models import Bin


class BinSerializer(ModelSerializer):
    class Meta:
        model = Bin
        fields = ('id', 'name', 'body')