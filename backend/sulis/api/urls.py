from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BinViewSet


bin_router = DefaultRouter()
bin_router.register(r'bins', BinViewSet)