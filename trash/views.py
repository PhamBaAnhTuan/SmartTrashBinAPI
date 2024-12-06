from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from trash.serializers import TrashSerializer, TrashTypeSerializer
from trash.models import Trash, TrashType

class TrashViewSet(viewsets.ModelViewSet):
   authentication_classes = [OAuth2Authentication]
   permission_classes = [IsAuthenticated]
   queryset = Trash.objects.all()
   serializer_class = TrashSerializer
   
   def get_permissions(self):
      if self.action in ['list', 'retrieve', 'create', 'update', 'partial_update']:
         return [AllowAny()]
      elif self.action in ['destroy']:
         return [IsAuthenticated()]
      return super().get_permissions()
   
class TrashTypeViewSet(viewsets.ModelViewSet):
   authentication_classes = [OAuth2Authentication]
   permission_classes = [IsAuthenticated]
   queryset = TrashType.objects.all()
   serializer_class = TrashTypeSerializer
   
   def get_permissions(self):
      if self.action in ['list', 'retrieve', 'create', 'update', 'partial_update']:
         return [AllowAny()]
      elif self.action in ['destroy']:
         return [IsAuthenticated()]
      return super().get_permissions()