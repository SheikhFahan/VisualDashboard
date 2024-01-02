from django.urls import path

from .views import CofferModelListCreateSerializerAPIView

urlpatterns = [
    path('coffer/',CofferModelListCreateSerializerAPIView.as_view() )
]
