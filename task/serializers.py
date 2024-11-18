from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

User= get_user_model()

class UserSerializer(serializers.ModelSerializer):
    re_password=serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True)

    password= serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model=User
        fields='__all__'
        extra_kwargs={
            'password':{'write_only':True},
            're_password':{'write_only':True}
        }

    def validate(self, attrs):
            max=10
            if len(attrs['password'])<max:
                raise serializers.ValidationError('Password must be at least 10 characters')
            if attrs['password']!=attrs['re_password']:
                raise serializers.ValidationError('Password and re_password must be same')
            return super().validate(attrs)
    def create(self,data):
         User.objects.create_user(
              **data
         )


class LoginSerializer(serializers.Serializer):
     email=serializers.EmailField()
     password=serializers.CharField(style={'input_type':'password'},write_only=True)




class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ['username','email', 'password']
        extra_kwargs={
            'password':{'write_only':True},
            'email':{'write_only':False, 'required':True},
            # 'bio':{'write_only': False, 'required': True}
            
        }



# my wrong user serializer code
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email']
#         extra_kwargs={
#                     'password':{'write_only':True, 'required':False},
#                     'email':{'read_only':True, 'required':False}

#                 }

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'


# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Register
#         fields='__all__'
