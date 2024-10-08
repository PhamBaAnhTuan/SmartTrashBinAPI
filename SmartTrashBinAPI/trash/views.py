from rest_framework import viewsets
from rest_framework.response import Response
from trash.serializers import TrashSerializer, TrashTypeSerializer
from trash.models import Trash, TrashType
from rest_framework.permissions import AllowAny

class TrashViewSet(viewsets.ModelViewSet):
   permission_classes = [AllowAny]
   queryset = Trash.objects.all()
   serializer_class = TrashSerializer
   
class TrashTypeViewSet(viewsets.ModelViewSet):
   permission_classes = [AllowAny]
   queryset = TrashType.objects.all()
   serializer_class = TrashTypeSerializer