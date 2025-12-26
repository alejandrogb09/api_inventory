from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory.views import ProductViewSet, MovementViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='product')
router.register(r'movements', MovementViewSet, basename='movement')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', obtain_auth_token),
]
