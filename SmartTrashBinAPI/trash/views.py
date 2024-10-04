from rest_framework import viewsets
from rest_framework.response import Response
from trash.serializers import TrashSerializer, TrashTypeSerializer
from trash.models import Trash, TrashType

class TrashViewSet(viewsets.ModelViewSet):
   queryset = Trash.objects.all()
   serializer_class = TrashSerializer
   
class TrashTypeViewSet(viewsets.ModelViewSet):
   queryset = TrashType.objects.all()
   serializer_class = TrashTypeSerializer