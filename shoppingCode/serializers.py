# Django REST Framework
from django.db.models import fields, query
from django.core.validators import RegexValidator

from rest_framework import serializers
from rest_framework.authtoken.models import Token

# Models
from shoppingCode.models import ShoppingCode

class ShoppingModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = ShoppingCode
        fields = [
            'id',
            'code',
            'user_id',
            ]

class ShoppingSaveSerializer(serializers.Serializer):
    
    code    = serializers.IntegerField(required=False, default=0)

    user_id = serializers.CharField(required=False)

    def create(self, data):
        shopping = ShoppingCode.objects.create(**data)
        return shopping
