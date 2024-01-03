from django.shortcuts import render

from datetime import datetime
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CofferModel
from .serializer import CofferModelSerializer, CofferFieldsSerializer
# Create your views here.

class CofferModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = CofferModel.objects.all()
    serializer_class = CofferModelSerializer

    def create(self, request, *args, **kwargs):
        # called upon the creation of object
        data = self.request.data
        new_data = []
        for data_item in data:
            added = data_item.get('added', '')
            published = data_item.get('published', '')

            if added:
                added = datetime.strptime(added, "%B, %d %Y %H:%M:%S")
                added_string = added.isoformat()
                data_item['added'] = added_string

            if published:
                published = datetime.strptime(published, "%B, %d %Y %H:%M:%S")
                published_string = added.isoformat()
                data_item['published'] = published_string

            for field_name, value in data_item.items():
                if value == "":
                    # You can set a default value or raise a validation error here
                    data_item[field_name] = None  # or return a default value
            new_data.append(data_item)
        
        serializer = CofferModelSerializer(data = new_data, many = True)
        if not serializer.is_valid():
            field_errors = serializer.errors
            print(serializer.errors)
            # for field_name, error_messages in field_errors.items():
                # print(f"Errors for {field_name}: {error_messages}")
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

        
class FieldsListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        instance = CofferModel.objects.first()
        serializer = CofferFieldsSerializer(instance)
        return Response(serializer.data)
        
class DynamicFieldDataListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        field = self.kwargs['field']
        instances = CofferModel.objects.all()
        field_data = [getattr(instance, field) for instance in instances if getattr(instance, field) is not None]

        return Response({
            field : field_data
        })
    
    

