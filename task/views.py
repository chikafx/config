from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import response, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, action


# # views for user registration
class CreateUserView(APIView):

    """
    this is a view used to create a user in this section

    NB:this view is not protected
    """
    @swagger_auto_schema(method="post", request_body=UserSerializer )
    @action(detail=True, methods=['post'])

    def post(self, request):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data.pop('re_password')
        serializer.save()

        return Response(serializer.data, status=201)






# my wrong create user code
# class UserRegistrationView(APIView):
#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return response.Response({'message':'user successfully created'})
#         return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserListView(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
    
    
    # my wrong code 
# class UserListView(generics.ListAPIView):
#     serializer_class=UserSerializer
#     queryset= UserList.objects.filter()


# views for login
class LoginView(APIView):
    """
    this is a view used to create a user in this section to login NB:this view is not protected
    """
    @swagger_auto_schema(method='post', request_body=UserSerializer)
    @action(detail=True, methods=['post'])

    def post(self, request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            user=authenticate(request,email=serializer.validated_data['email'],
                              password=serializer.validated_data['password'])
            if user:
                try:
                    refresh_token=RefreshToken.for_user(user)
                    data={}
                    data['id']=user.pk
                    data['first_name']=user.first_name
                    data['last_name']=user.last_name
                    data['access_token']=str(refresh_token.access_token)
                    data['refresh_token']=str(refresh_token)

                    return Response(data, status=200)
                except Exception as error:
                    return Response(
                        {
                            'error': f"{error}"
                        },
                        status=400
                    ) 
            else:
                    data={
                        'error': 'invalid login credentials'
                    }
                    return Response(data, status=401)
        else:
                data={
                    'error':serializer.errors
                }
                return Response(data, status=400)





# my wrong login view code

# class loginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         try:
#             user = User.objects.get(username=username)
#             if user.check_password(password):
#                 return response.Response({'message': 'user logged in successfully'})
#             else:
#                 return response.Response({'message': 'invalid password'}, status=status.HTTP_400_BAD_REQUEST)
#         except User.DoesNotExist:
#             return response.Response({'message': 'invalid username'}, status=status.HTTP_400_BAD_REQUEST)
        
# views for logout
class logoutView(APIView):
    def post(self, request):
        return response.Response({'message':'logout successful'})
    
# views for creating new task
class TaskCreateView(generics.CreateAPIView):
     serializer_class=TaskSerializer
     queryset= Task.objects.filter()
        
#  views for updating task
class UpdateTaskView(generics.UpdateAPIView):
     serializer_class= TaskSerializer
     queryset=Task.objects.all()
     lookup_field='pk'

class ListTaskView(generics.ListAPIView):
     serializer_class=TaskSerializer
     queryset=Task.objects.filter()

class DeleteTaskView(generics.DestroyAPIView):
     serializer_class= TaskSerializer
     queryset= Task.objects.all()
     lookup_field='pk'
        



