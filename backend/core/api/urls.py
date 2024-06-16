from rest_framework.routers import DefaultRouter
from sulis.api.urls import bin_router
from django.urls import path, include

router = DefaultRouter()
# bin
router.registry.extend(bin_router.registry)

urlpatterns = [
    path('', include(router.urls))
]
