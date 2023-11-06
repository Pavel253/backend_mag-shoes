import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Shoes

class ShoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoes
        fields = "__all__"