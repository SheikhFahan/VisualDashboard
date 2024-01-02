from rest_framework import serializers

from datetime import datetime

from .models import CofferModel

class CofferModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CofferModel
        fields = '__all__'
