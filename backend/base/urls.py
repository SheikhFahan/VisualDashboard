from django.urls import path

from .views import CofferModelListCreateAPIView, FieldsListAPIView, DynamicFieldDataListAPIView

urlpatterns = [
    path('coffer/',CofferModelListCreateAPIView.as_view()),
    path('fields/',FieldsListAPIView.as_view()),
    path('<str:field>/fetch/',DynamicFieldDataListAPIView.as_view()),



]
