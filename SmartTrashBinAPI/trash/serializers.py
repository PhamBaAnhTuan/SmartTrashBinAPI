from . import models
from rest_framework import serializers

class TrashSerializer(serializers.ModelSerializer):
   class Meta:
      model = models.Trash
      fields = '__all__'
      
class TrashTypeSerializer(serializers.ModelSerializer):
   class Meta:
      model = models.TrashType
      fields = '__all__'