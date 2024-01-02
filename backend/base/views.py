from django.shortcuts import render

from datetime import datetime
from rest_framework import generics, status
from rest_framework.response import Response

from .models import CofferModel
from .serializer import CofferModelSerializer
# Create your views here.

class CofferModelListCreateSerializerAPIView(generics.ListCreateAPIView):
    serializer_class = CofferModelSerializer
    queryset = CofferModel.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
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
        serializer = CofferModelSerializer(data = data, many = True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)