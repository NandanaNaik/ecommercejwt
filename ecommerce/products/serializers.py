# products/serializers.py

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from .models import Product, UserDetails

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    emp_name = serializers.CharField(required=True)

    def validate(self, attrs):
        credentials = {
            'emp_name': attrs.get('emp_name'),
            'password': attrs.get('password')
        }

        user = authenticate(emp_name=credentials['emp_name'], password=credentials['password'])
        if user:
            data = super().validate(attrs)
            refresh = self.get_token(user)
            
            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)

            # Add extra responses here
            data['emp_id'] = user.emp_id
            data['emp_name'] = user.emp_name
            return data
        else:
            raise serializers.ValidationError('Invalid credentials')

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['emp_id'] = user.emp_id
        token['emp_name'] = user.emp_name
        return token

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# serializers.py

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from .models import UserDetails

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    emp_name = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        credentials = {
            'emp_name': attrs.get('emp_name'),
            'password': attrs.get('password')
        }

        user = authenticate(**credentials)
        if user:
            data = super().validate(attrs)
            refresh = self.get_token(user)
            
            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)

            # Add extra responses here if needed
            data['emp_id'] = user.emp_id
            data['emp_name'] = user.emp_name
            return data
        else:
            raise serializers.ValidationError('Invalid credentials')
