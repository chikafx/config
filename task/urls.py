from django.urls import path
from .views import *



urlpatterns=[
    path('create/', CreateUserView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', logoutView.as_view()),
    path('list_user/', UserListView.as_view()),
    path('task/', TaskCreateView.as_view()),
    path('update_task/<int:pk>/', UpdateTaskView.as_view()),
    path('list_task/', ListTaskView.as_view()),
    path('delete_task/<int:pk>/', DeleteTaskView.as_view()),
]