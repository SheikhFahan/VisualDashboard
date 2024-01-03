from rest_framework import serializers

from datetime import datetime

from .models import CofferModel

class CofferModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CofferModel
        fields = '__all__'
        extra_kwargs = {field: {'required': False} for field in CofferModel._meta.get_fields()}



class CofferFieldsSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        field_names = {f'{field.name}': field.name for field in instance._meta.get_fields()}

        return field_names
    
class DynamicFieldSerializer(serializers.BaseSerializer):
    dynamic_field = serializers.ListField()
