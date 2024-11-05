from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = (
         'id', 
         'is_superuser',
         'username',
         'password',
         'first_name',
         'last_name',
      )

   def create(self, validated_data):
      user = User(
         username=validated_data['username'],
         password=validated_data['password']
      )
      user.set_password(validated_data['password'])
      user.save()
      return user