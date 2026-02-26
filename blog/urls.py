from .views import *
from django.urls import path, include
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'posts', PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
]