from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from shoppingCode import views as shopping_views

router = DefaultRouter()
router.register(r'shoppingCode', shopping_views.ShoppingViewSet, basename='shopping')

urlpatterns = [
    # Contacts views
    path('', include(router.urls))
]