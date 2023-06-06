# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Serializers
from shoppingCode.serializers import ShoppingModelSerializer, ShoppingSaveSerializer

# Models
from shoppingCode.models import ShoppingCode

class ShoppingViewSet(viewsets.GenericViewSet):

    """
    Authentication is needed for this methods
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ShoppingCode.objects.filter(is_active=True)
    serializer_class = ShoppingModelSerializer

    #actualiza datos de una tienda
    @action(detail=False, methods=['post'])
    def createShoppingCode(self, request, format=None):
        try: 
            id = request.user.id
            if not ShoppingCode.objects.filter(user_id = id):
                request.data._mutable = True
                request.data['user_id'] = id
                serializer = ShoppingSaveSerializer(data = request.data)
                if serializer.is_valid(raise_exception=True):
                    code = serializer.save()
                    code = ShoppingModelSerializer(code).data
                    return Response({"message": 'codigo creado', "data": code},status=status.HTTP_201_CREATED)
        except :
            return Response({"message": 'error al crear codigo'},status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['put'])
    def updateShoppingCode(self, request, format=None):
        try:
            id = request.user.id
            code = ShoppingCode.objects.get(user_id = id)
            code.code = code.code + 1;
            code.save(); 
            serializer = ShoppingModelSerializer(code).data
            return Response({"message": 'codigo actualizado', "data": serializer},status=status.HTTP_201_CREATED)
        except:
            return Response({"message": 'error al actualizar codigo'},status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def getShoppingCode(self, request, format=None):
        try:
            id = request.user.id
            code = ShoppingCode.objects.get(user_id = id)
            code = ShoppingModelSerializer(code).data
            return Response({"message": 'codigo compra', "data": code},status=status.HTTP_200_OK)
        except:
            return Response({"message": 'error al obtener codigo'},status=status.HTTP_400_BAD_REQUEST)

