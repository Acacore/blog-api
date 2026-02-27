from .views import *
from django.urls import path, include
from rest_framework import routers

# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'posts', PostViewSet)


urlpatterns = [
    # Redirect root to Swagger UI
    # API routes
    path('', include(router.urls)),
]