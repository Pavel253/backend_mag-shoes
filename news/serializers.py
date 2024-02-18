import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"