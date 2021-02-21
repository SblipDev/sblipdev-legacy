from rest_framework import serializers
from .models import CustomUser
from rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name','description', 'role', 'is_authenticated']


class CustomRegisterSerializer(RegisterSerializer):
    role = serializers.CharField(max_length=30)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=600)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)

        user.role = self.data.get('role')
        user.description = self.data.get('description')
        user.first_name = self.data.get('first_name')
        user.last_name = self.data.get('last_name')
        user.save()
        return user



